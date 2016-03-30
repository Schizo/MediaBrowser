import os
import json
import shutil
import time

if __debug__:
    rootPath = "Categories/"
else:
    rootPath = "W:/Categories/"

if __debug__:
    pathCachePath = "../resources/pathcache_debug.json"
else:
    pathCachePath = "W:/DB/pathcache.json"

appPath = {"photoshop":"C:/Program Files/Adobe/Adobe Photoshop CC 2015/Photoshop.exe",
           "rv":"C:/Program Files/Tweak/RV/bin/rv.exe",
           "explorer": "C:/Windows/explorer.exe",
           "djv": "C:/Program Files/djv-1.1.0-Windows-64/bin/djv_view.com"}

showConfig = {"startCategory": 'Fire/Flames'}
currentCategory = "Fire/Flames"
class Meta:
    PATH = 0
    WIDTH = 1
    HEIGHT = 2
    FPS = 3
    START_FRAME = 4
    END_FRAME = 5
    PROJECT_NAME = 6

thumbnails  = {
	"numOfThumbnails":50,
    "width":200,
    "height":160
}

about = {"Author":"Yafes Sahin", "Idea":["Julian Weiss", "Yafes Sahin"], "Additional Coding":"Marcel Ruegenberg", "name":"Elementsbrowser", "version": "v. 0.2"}

def locationPath(categoryName, fileName):
    return os.path.join(rootPath, categoryName, fileName).replace("\\","/")

def thumbPath(categoryName, fileName):
    return os.path.join(rootPath, categoryName, fileName, "Thumbnails", "").replace("\\","/")

def proxyPath(categoryName, fileName):
    return os.path.join(rootPath, categoryName, fileName, "Proxy", "{}.####.jpg".format(fileName)).replace("\\","/")

def sourcePath(categoryName, fileName):
    # replacing backslashes is necessary because Nuke doesn't do well with them
    return os.path.join(rootPath, categoryName, fileName, "Source", "{}.####.exr".format(fileName)).replace("\\","/")

# theoretically slow for startup, but in practice avoid premature optimization
print("Loading file {}".format(pathCachePath))
with open(pathCachePath,'r') as dbfile:
    pathCache = json.load(dbfile)

def persistPathCache():
    global pathCache
    global pathCachePath

    # backup copy
    timestamp = int(time.time())
    (fn,ext) = os.path.splitext(os.path.split(pathCachePath)[1])
    shutil.copy(pathCachePath,os.path.split(pathCachePath)[0] + "/bak/" + "{}.{}.{}".format(fn, str(timestamp), ext))

    with open(pathCachePath, 'w') as dbfile:
         json.dump(pathCache, dbfile, indent=4)


nextID0 = None
def nextID():
    global nextID0 # ya ya, I know... globals are evil
    if nextID0:
        nextID0 += 1
    else:
        nextID0 = 0
        # go through the path cache and find an unused ID
        for p in pathCache:
            for it in pathCache[p]:
                theID = pathCache[p][it]["id"]
                if theID >= nextID0:
                    nextID0 = theID + 1
    return nextID0

def removeItem(category, filename):
    # TODO: implemented
    #       1) delete from DB (maybe just set isVisible to 0 (and implement that this flag is actually used))
    #       2) persist the DB
    #       3) update the view
    print("remove {} {}".format(category,filename))

data = [
    ("Blood", []),
    ("Cloth", []),
    ("Debug", []),
    ("Dirt", []),
    ("Debris", []),
    ("Glass", []),
    ("Feathers", []),
    ("Fire", [
        ("Flames", []),
        ("Sparks", []),
        ("Smoke", [])
        ]),
    ("Leaves", []),
    ("Lensflares", [
        ("Bokeh", []),
        ("Lightleaks", []),
        ("Misc", []),
        ("Rays", [])
        ]),
    ("Pollen", []),
    ("Scenic", []),
    ("Smoke_and_Fog", []),
    ]
