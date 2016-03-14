# TODO: cleanup imports
import os, sys
import nuke
import time
import tempfile
import subprocess, multiprocessing
import math

# how to use: runConverter.bat [input-folder-name] [category name]

# some extensions don't make much sense for high-quality work. we include them nevertheless
image_extensions = ["exr","hdr","ari","cin","dpx","tif","tga","jpg","jpeg","png"]
mov_extensions = ["mov","mp4"]
valid_extensions = image_extensions + mov_extensions

# output = outputpath/Categories/Category/fileprefix
outputpath = "W:\\Categories"

thumb_width = 200

class SequenceImg:
    def __init__(self, prefix, range_start, range_end, ext):
        self.prefix = prefix
        self.range = (range_start, range_end)
        self.ext = ext

    def __str__(self):
        return self.prefix + ".[" + str(self.range[0]).zfill(4) + "-" + str(self.range[1]).zfill(4) + "]." + self.ext

    def inputpath(self):
        return self.prefix + ".####." + self.ext + " " + str(self.range[0]).zfill(4) + "-" + str(self.range[1]).zfill(4)

    def basename(self):
        return self.prefix


class SequenceMov:
    def __init__(self, filename, ext):
        self.filename = filename
        self.ext = ext

    def __str__(self):
        return self.filename + "." + self.ext

    def inputpath(self):
        return self.filename + "." + self.ext

    def basename(self):
        return self.filename

# Converts the image sequence found in `input_folder`
# `input_folder` is the absolute path to a folder containing images
# `category_name` is the name of a folder in outputpath
# `thread_count` is the number of processes to use. If this is 0, `multiprocessing.cpu_count()` is used.
# `progress_callback` is called with the current progress (between 0 and 1) as the argument
# `done_callback` is called when the whole conversion is finished.
#
# This function returns as soon as the conversion was started (ie after a few seconds instead of minutes)
def convertSequence(input_folder, category_name, thread_count=0, progress_callback=None, done_callback=None):
    if not os.path.exists("W:\\Categories\\" + category_name):
        print( "Invalid category name ", category_name)
        return
    if not os.path.exists(input_folder):
        print("Invalid input folder ", input_folder)
        return
    if thread_count == 0:
        thread_count = multiprocessing.cpu_count()

    # potential sequence files
    unsorted_files = filter(lambda f: os.path.splitext(f)[1][1:] in valid_extensions, os.listdir(input_folder))

    # Sort by extension first to avoid the following failure case in the sequence-finding code below:
    # foo.0001.exr
    # foo.0001.jpg in same folder
    files = sorted(unsorted_files, key=lambda f: os.path.splitext(f)[::-1])

    print "Found ", len(files), " movie/image files"

    # Find all sequences.
    sequences = []
    last_prefix = None
    last_ext    = None
    seq_start = 0
    seq_end   = 0
    counter = len(files)
    for file in files:
        components = file.split(".")
        ext = os.path.splitext(file)[1][1:]
        new_seq = False
        is_movie = False
        is_img = False
        if len(components) >= 3 and ext in image_extensions:
            prefix = ".".join(components[0:-2])
            is_img = True
        elif len(components) == 2 and ext in mov_extensions:
            prefix = components[0]
            is_movie = True

        # new sequence start => insert the last sequence
        if prefix != last_prefix or ext != last_ext:
            if not (last_prefix is None):
                sequences.append(SequenceImg(last_prefix, seq_start, seq_end, last_ext))
            new_seq = True

        # handle the current file
        if is_movie: # movies are treated as single-file sequences
            prefix = components[0]
            sequences.append(SequenceMov(prefix,ext))
        elif is_img:
            frame  = components[-2]
            if new_seq:
                seq_start = int(frame)
                last_prefix = prefix
                last_ext = ext
            seq_end   = int(frame)

            if counter == 1: # last file
                sequences.append(SequenceImg(last_prefix, seq_start, seq_end, last_ext))

        counter -= 1

    print("Found sequences: ")
    for seq in sequences:
        print seq

    # conversion
    nuke.nodePaste("converter.nk")
    reader = nuke.toNode("Read1")
    source_writer = nuke.toNode("Write_Source")
    proxy_writer = nuke.toNode("Write_Proxy")
    thumb_writer = nuke.toNode("Write_Thumb")
    thumb_retime = nuke.toNode("Thumb_Retime")
    thumb_reformat = nuke.toNode("Reformat_Thumb")

    tempfiles = []
    tempdir   = tempfile.mkdtemp()
    print ("tempdir is ", tempdir)

    # Generate Nuke scripts with the correct paths etc in a temporary directory
    nxttmpfile = 0
    for seq in sequences:
        reader['file'].fromUserText(os.path.join(input_folder, seq.inputpath()))

        # determine info from Read node
        input_dims = (int(reader.format().width()), int(reader.format().height()))
        aspect_ratio = input_dims[0] / float(input_dims[1])
        thumb_height = int(thumb_width / aspect_ratio)
        input_range = (int(nuke.toNode("Read1")['first'].getValue()), int(nuke.toNode("Read1")['last'].getValue()))

        # Set thumbnail retiming
        thumb_retime['input.first'].setValue(input_range[0])
        thumb_retime['input.last'].setValue(input_range[1])
        thumb_count = int(thumb_retime['output.last'].value())

        # Set thumbnail format
        thumb_reformat['format'].setValue(nuke.addFormat(str(thumb_width) + " " + str(thumb_height) + " 1"))

        # Generate output dirs
        out_root = os.path.join(outputpath, category_name, seq.basename())
        dirs = (os.path.join(out_root, "Source"), os.path.join(out_root, "Proxy"), os.path.join(out_root, "Thumbnails"))
        for dir in dirs:
            if not os.path.exists(dir):
                os.makedirs(dir)
        (source_dir, proxy_dir, thumb_dir) = dirs

        # Set output names
        source_writer['file'].fromUserText(os.path.join(source_dir, seq.basename() + ".####." + "exr"))
        proxy_writer['file'].fromUserText(os.path.join(proxy_dir, seq.basename() + ".####." + "jpg"))
        thumb_writer['file'].fromUserText(os.path.join(thumb_dir, seq.basename() + ".####." + "jpg"))
        # proxyWriter('_jpeg_quality').setValue(0.9) # not needed since we do this kind of thing in the predefined nuke script itself

        filepath = os.path.join(tempdir, str(nxttmpfile) + ".nk")
        nuke.scriptSaveAs(filepath)
        tempfiles.append((filepath, "Write_Thumb", 1, thumb_count))
        tempfiles.append((filepath, "Write_Proxy", input_range[0], input_range[1]))
        tempfiles.append((filepath, "Write_Source", input_range[0], input_range[1]))
        nxttmpfile += 1

    print "Starting conversion..."

    nuke.threading.Thread( target=do_conversion, args=(tempfiles, tempdir, thread_count, progress_callback, done_callback)).start()
    print "Started conversion"

def do_conversion(tempfiles, tempdir, thread_count, progress_callback, done_callback):
    tmpfilecount = len(tempfiles)
    cur_progress = 0

    # Execute in subprocesses
    for tmpfile in tempfiles:
        (fn, writer, start, end) = tmpfile
        frames = end - start
        frames_per_thread = int(math.ceil(frames / float(thread_count)))

        cur_processes = []
        for i in range(0, thread_count):
            cur_start = start + frames_per_thread * i
            if cur_start > end:
                break
            cur_end = min(end, cur_start + frames_per_thread)
            p = subprocess.Popen([nuke.env["ExecutablePath"], "-X", writer, fn, str(cur_start) + "-" + str(cur_end)])
            cur_processes.append(p)
        # wait for all thread_count processes to finish
        for p in cur_processes:
            p.wait()
            cur_progress += 1.0 / (tmpfilecount * thread_count)
            if progress_callback is not None:
                nuke.executeInMainThread(progress_callback, cur_progress)



    # Cleanup
    os.unlink(tempdir)

    if done_callback is not None:
        nuke.executeInMainThread(done_callback)

if __name__ == "__main__":
    def progress(p):
        print ("PROGRESS ", str(p))
    def done():
        print "DONE"
    convertSequence(sys.argv[1], sys.argv[2], 4, progress, done) # maybe limit CPU count? (because the HDD becomes the bottleneck)
