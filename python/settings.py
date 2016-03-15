import os
import json

if __debug__:
    rootPath = "Categories/"
else:
    rootPath = "W:/Categories/"

if __debug__:
    pathCachePath = "../resources/pathcache_debug.json"
else:
    pathCachePath = "W:/DB/pathcache.json"

appPath = {"photoshop":"", "rv":"", "vlc":""}

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
    ("Leafes", []),
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
