from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4.QtGui import *
import subprocess
import threading
import settings

class FileBrowseWidget(QtGui.QWidget):
    def __init__(self, parent, do_folder=False):
        super(FileBrowseWidget, self).__init__(parent)

        self.fnText = QtGui.QLineEdit("")
        self.browseButton = QtGui.QPushButton("Browse")
        self.browseButton.clicked.connect(self.browseButtonClicked)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.fnText)
        layout.addWidget(self.browseButton)
        self.setLayout(layout)

        self.do_folder = do_folder

    def browseButtonClicked(self):
        if self.do_folder:
            fN = QtGui.QFileDialog.getExistingDirectory(self, 'Browse', '.')
        else:
            fN = QtGui.QFileDialog.getOpenFileName(self, 'Browse', '.', "Images (*.exr *.hdr *.ari *.cin *.dpx *.tif *.tga *.jpg *.jpeg *.png);;Movies (*.mp4 *.mov)")
        if fN:
            self.fnText.setText(fN)

def findCategories(prePath, elements):
    res = []
    for text, children in elements:
        itemTxt = prePath + str(text)
        res.append(itemTxt)
        if children:
            res = res + findCategories(itemTxt + "/", children)
    return res

# TODO: cancel button
class SequenceAdder(QtGui.QFrame):
    logUpdate = pyqtSignal(str, name='logUpdate')

    def __init__(self, parent):
        self.parent = parent
        super(SequenceAdder, self).__init__(parent)

        self.process = None

        # self.fileBrowser = FileBrowseWidget(self)
        self.fileBrowser = FileBrowseWidget(self, do_folder=True)
        self.categoryChooser = QtGui.QComboBox()
        categories = findCategories("", settings.data)
        for c in categories:
            self.categoryChooser.addItem(c)
        self.convertButton = QtGui.QPushButton("Convert")
        self.convertButton.clicked.connect(self.convertClicked)
        self.cancelButton = QtGui.QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.cancelClicked)
        self.cancelButton.setEnabled(False)

        self.lbl = QtGui.QLabel("")

        self.logView = QtGui.QPlainTextEdit()
        self.logView.setPlainText("")
        self.logView.setReadOnly(True)

        layout = QtGui.QFormLayout()
        layout.addRow("Input Folder", self.fileBrowser)
        layout.addRow("Category", self.categoryChooser)
        layout.addRow(self.convertButton)
        layout.addRow(self.cancelButton)
        layout.addRow(self.lbl)
        layout.addRow(self.logView)

        self.setLayout(layout)

        self.logView.appendPlainText("")

    def done(self):
        self.lbl.setText("")
        self.convertButton.setEnabled(True)
        self.cancelButton.setEnabled(False)

    def callConvert(self, dir, cat):
        self.process = subprocess.Popen(("C:\Program Files\Nuke9.0v7\Nuke9.0.exe", "-t", "convertMaterial.py", dir, cat), bufsize=1, stdout=subprocess.PIPE)
        # for l in iter(self.process.stdout.readline, b''):
        #

        with self.process.stdout:
             for line in iter(self.process.stdout.readline, b''):
                 self.logUpdate.emit(str(line))
                 # self.logView.appendPlainText(str(line))
                 # print line
        self.process.wait()

    def onLogUpdate(self, line):
        self.logView.appendPlainText(line)

    def convertClicked(self):
        # TODO: get progress and done as well as ability to cancel
        #       use  Popen.communicate() (see https://docs.python.org/2/library/subprocess.html#subprocess.Popen.poll)
        #       also http://stackoverflow.com/questions/375427/non-blocking-read-on-a-subprocess-pipe-in-python/4896288#4896288

        self.logUpdate.connect(self.onLogUpdate)

        threading.Thread(target=self.callConvert, args=(str(self.fileBrowser.fnText.text()), str(self.categoryChooser.currentText())) ).start()

        self.logView.setPlainText("")

        # TODO: proper progress bar etc
        # https://gist.github.com/kaotika/e8ca5c340ec94f599fb2
        self.lbl.setText("converting... please wait, this will take a while")

        self.convertButton.setEnabled(False)
        self.cancelButton.setEnabled(True)

    def cancelClicked(self):
        if self.process:
            self.process.terminate() # not very elegant, but ok
        print "cancel"
        self.done()
