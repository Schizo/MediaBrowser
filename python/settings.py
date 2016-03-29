import os

if __debug__:
    rootPath = "Categories/"
else:
    rootPath = "W:/Categories/"

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

about = {"Author":"Yafes Sahin", "Idea":["Julian Weiss", "Yafes Sahin"], "name":"Elementsbrowser", "version": "v. 0.2"}

def thumbPath(categoryName, fileName):
    return os.path.join(rootPath, categoryName, fileName, "Thumbnails", "").replace("\\","/")

def proxyPath(categoryName, fileName):
    return os.path.join(rootPath, categoryName, fileName, "Proxy", "{}.####.jpg".format(fileName)).replace("\\","/")

def sourcePath(categoryName, fileName):
    # replacing backslashes is necessary because Nuke doesn't do well with them
    return os.path.join(rootPath, categoryName, fileName, "Source", "{}.####.exr".format(fileName)).replace("\\","/")

pathCache = {
  "Debris": { },
  "Glass": { },
  "Lensflares/Misc": {
    "A019C016_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 287
    },
    "A019C019_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 289
    },
    "A019C018_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 288
    },
    "A018C037_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 281
    },
    "A018C035_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 280
    },
    "A019C013_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 286
    },
    "A019C001_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 283
    },
    "A020C005_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 290
    },
    "A018C050_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 282
    },
    "A019C008_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 284
    },
    "A019C009_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 285
    },
    "A018C034_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 279
    }
  },
  "Dirt": {
    "VFX_Plates_Cam_9624_CineF14_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 64
    },
    "VFX_Plates_Cam_9624_CineF21_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 71
    },
    "A008C002_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 55
    },
    "VFX_Plates_Cam_9624_CineF17_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 67
    },
    "VFX_Plates_Cam_9624_CineF23_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 73
    },
    "VFX_Plates_Cam_9624_CineF11_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 61
    },
    "VFX_Plates_Cam_9624_CineF54_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 82
    },
    "VFX_Plates_Cam_9624_CineF49_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 77
    },
    "A008C006_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 59
    },
    "VFX_Plates_Cam_9624_CineF24_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 74
    },
    "VFX_Plates_Cam_9624_CineF10_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 60
    },
    "VFX_Plates_Cam_9624_CineF22_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 72
    },
    "VFX_Plates_Cam_9624_CineF53_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 81
    },
    "VFX_Plates_Cam_9624_CineF25_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 75
    },
    "VFX_Plates_Cam_9624_CineF51_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 79
    },
    "VFX_Plates_Cam_9624_CineF9_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 83
    },
    "VFX_Plates_Cam_9624_CineF20_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 70
    },
    "VFX_Plates_Cam_9624_CineF13_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 63
    },
    "VFX_Plates_Cam_9624_CineF18_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 68
    },
    "VFX_Plates_Cam_9624_CineF12_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 62
    },
    "A008C003_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 56
    },
    "VFX_Plates_Cam_9624_CineF15_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 65
    },
    "VFX_Plates_Cam_9624_CineF26_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 76
    },
    "A008C001_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 54
    },
    "A008C004_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 57
    },
    "A008C005_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 58
    },
    "VFX_Plates_Cam_9624_CineF52_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 80
    },
    "VFX_Plates_Cam_9624_CineF19_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 69
    },
    "VFX_Plates_Cam_9624_CineF50_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 78
    },
    "VFX_Plates_Cam_9624_CineF16_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 66
    }
  },
  "Fire/Sparks": {
    "A004C006_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 110
    },
    "A004C001_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 109
    },
    "A003C008_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 107
    },
    "A003C009_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 108
    },
    "A003C006_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 106
    }
  },
  "Scenic": {
    "A001C001_140913_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 154
    },
    "A001C003_140913_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 156
    },
    "A001C004_140913_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 157
    },
    "A007C012_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 164
    },
    "A001C008_140913_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 161
    },
    "A001C002_140913_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 155
    },
    "A001C006_140913_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 159
    },
    "A001C005_140913_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 158
    },
    "A001C007_140913_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 160
    },
    "A001C009_140913_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 162
    },
    "A001C010_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 163
    }
  },
  "Fire/Smoke": {
    "A003C001_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 105
    }
  },
  "Lensflares/Rays": {
    "A018C033_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 297
    },
    "A018C026_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 292
    },
    "A018C031_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 295
    },
    "A018C028_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 293
    },
    "A020C001_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 311
    },
    "A019C032_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 309
    },
    "A018C045_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 299
    },
    "A019C026_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 308
    },
    "A019C017_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 305
    },
    "A018C047_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 301
    },
    "A018C051_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 302
    },
    "A018C025_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 291
    },
    "A019C025_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 307
    },
    "A018C032_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 296
    },
    "A018C044_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 298
    },
    "A020C011_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 314
    },
    "A020C010_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 313
    },
    "A018C029_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 294
    },
    "A018C052_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 303
    },
    "A019C034_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 310
    },
    "A019C006_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 304
    },
    "A020C007_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 312
    },
    "A019C022_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 306
    },
    "A018C046_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 300
    }
  },
  "Lensflares/Bokeh": {
    "A019C007_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 248
    },
    "A019C005_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 247
    },
    "A020C008_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 251
    },
    "A018C053_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 244
    },
    "A018C041_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 243
    },
    "A020C003_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 250
    },
    "A020C009_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 252
    },
    "A019C004_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 246
    },
    "A018C030_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 241
    },
    "A019C023_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 249
    },
    "A018C040_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 242
    },
    "A019C002_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 245
    }
  },
  "Feathers": {
    "VFX_Plates_Cam_9624_CineF1_FPS500": {
        "numOfFrames": 1001,
        "height": 1600,
        "width": 2560,
        "fps": 500,
        "isVisible": "",
        "startFrame": 1001,
        "id": 85
    },
    "VFX_Plates_Cam_9624_CineF3_FPS100": {
        "numOfFrames": 1001,
        "height": 1600,
        "width": 2560,
        "fps": 100,
        "isVisible": "",
        "startFrame": 1001,
        "id": 87
    },
    "VFX_Plates_Cam_9624_CineF4_FPS100": {
        "numOfFrames": 1001,
        "height": 1600,
        "width": 2560,
        "fps": 100,
        "isVisible": "",
        "startFrame": 1001,
        "id": 88
    },
    "VFX_Plates_Cam_9624_CineF6_FPS50": {
        "numOfFrames": 1001,
        "height": 1600,
        "width": 2560,
        "fps": 50,
        "isVisible": "",
        "startFrame": 1001,
        "id": 90
    },
    "VFX_Plates_Cam_9624_CineF2_FPS500": {
        "numOfFrames": 1001,
        "height": 1600,
        "width": 2560,
        "fps": 500,
        "isVisible": "",
        "startFrame": 1001,
        "id": 86
    },
    "VFX_Plates_Cam_9624_CineF8_FPS100": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 100,
        "isVisible": "",
        "startFrame": 1001,
        "id": 92
    },
    "VFX_Plates_Cam_9624_CineF65_FPS50": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 50,
        "isVisible": "",
        "startFrame": 1001,
        "id": 89
    },
    "VFX_Plates_Cam_9624_CineF7_FPS50": {
        "numOfFrames": 1001,
        "height": 1600,
        "width": 2560,
        "fps": 50,
        "isVisible": "",
        "startFrame": 1001,
        "id": 91
    }
  },
  "Debug": {
    "A005C002_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 112
    }
  },
  "Cloth": {
    "A002C018_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 46
    },
    "A002C006_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 34
    },
    "A002C020_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 48
    },
    "A002C003_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 31
    },
    "A002C002_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 30
    },
    "A002C007_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 35
    },
    "A002C008_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 36
    },
    "A002C016_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 44
    },
    "A002C024_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 52
    },
    "A002C012_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 40
    },
    "A002C017_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 45
    },
    "A002C023_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 51
    },
    "A002C009_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 37
    },
    "A002C015_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 43
    },
    "A002C010_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 38
    },
    "A002C011_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 39
    },
    "A002C004_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 32
    },
    "A002C013_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 41
    },
    "A002C021_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 49
    },
    "A002C019_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 47
    },
    "A002C014_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 42
    },
    "A002C005_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 33
    },
    "A002C001_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 29
    },
    "A002C022_140913_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 50
    }
  },
  "Fire/Flames": {
    "A004C009_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 104
    },
    "A003C004_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 95
    },
    "A003C002_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 93
    },
    "A004C004_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 100
    },
    "A004C008_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 103
    },
    "A004C005_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 101
    },
    "A003C007_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 97
    },
    "A004C007_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 102
    },
    "A003C005_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 96
    },
    "A003C003_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 94
    },
    "A004C003_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 99
    },
    "A004C002_140913_FPS60": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 98
    }
  },
  "Blood": {
    "VFX_Plates_Cam_9624_CineF67_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 25
    },
    "VFX_Plates_Cam_9624_CineF71_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 28
    },
    "VFX_Plates_Cam_9624_CineF60_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 19
    },
    "VFX_Plates_Cam_9624_CineF35_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 9
    },
    "VFX_Plates_Cam_9624_CineF68_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 26
    },
    "VFX_Plates_Cam_9624_CineF27_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 1
    },
    "VFX_Plates_Cam_9624_CineF59_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 18
    },
    "VFX_Plates_Cam_9624_CineF65_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 23
    },
    "VFX_Plates_Cam_9624_CineF57_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 16
    },
    "VFX_Plates_Cam_9624_CineF39_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 13
    },
    "VFX_Plates_Cam_9624_CineF63_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 21
    },
    "VFX_Plates_Cam_9624_CineF61_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 20
    },
    "VFX_Plates_Cam_9624_CineF32_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 6
    },
    "VFX_Plates_Cam_9624_CineF38_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 12
    },
    "VFX_Plates_Cam_9624_CineF30_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 4
    },
    "VFX_Plates_Cam_9624_CineF64_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 22
    },
    "VFX_Plates_Cam_9624_CineF58_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 17
    },
    "VFX_Plates_Cam_9624_CineF37_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 11
    },
    "VFX_Plates_Cam_9624_CineF29_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 3
    },
    "VFX_Plates_Cam_9624_CineF56_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 15
    },
    "VFX_Plates_Cam_9624_CineF28_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 2
    },
    "VFX_Plates_Cam_9624_CineF31_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 5
    },
    "VFX_Plates_Cam_9624_CineF34_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 8
    },
    "VFX_Plates_Cam_9624_CineF36_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 10
    },
    "VFX_Plates_Cam_9624_CineF40_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 14
    },
    "VFX_Plates_Cam_9624_CineF33_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 7
    },
    "VFX_Plates_Cam_9624_CineF66_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 24
    },
    "VFX_Plates_Cam_9624_CineF70_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 27
    }
  },
  "Pollen": {
    "A007C027_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 152
    },
    "A007C028_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 153
    },
    "A007C025_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 150
    },
    "A007C026_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 151
    }
  },
  "Lensflares/Lightleaks": {
    "A020C006_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 278
    },
    "A018C049_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 259
    },
    "A020C002_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 276
    },
    "A019C027_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 270
    },
    "A019C014_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 265
    },
    "A018C054_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 260
    },
    "A019C029_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 272
    },
    "A018C039_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 255
    },
    "A019C015_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 266
    },
    "A019C030_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 273
    },
    "A019C011_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 263
    },
    "A019C003_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 261
    },
    "A020C004_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 277
    },
    "A018C038_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 254
    },
    "A019C012_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 264
    },
    "A018C048_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 258
    },
    "A019C031_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 274
    },
    "A019C028_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 271
    },
    "A019C021_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 268
    },
    "A019C033_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 275
    },
    "A018C043_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 257
    },
    "A019C020_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 267
    },
    "A018C036_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 253
    },
    "A018C042_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 256
    },
    "A019C024_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 269
    },
    "A019C010_150207_R3FI_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 262
    }
  },
  "Leafes": {
    "A007C005_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 122
    },
    "A007C009_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 126
    },
    "VFX_Plates_Cam_9624_CineF41_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 141
    },
    "A007C010_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 127
    },
    "A007C011_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 128
    },
    "A007C014_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 130
    },
    "A007C002_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 119
    },
    "A007C018_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 134
    },
    "A007C023_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 139
    },
    "A005C003_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 113
    },
    "VFX_Plates_Cam_9624_CineF47_FPS120": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 147
    },
    "A007C017_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 133
    },
    "VFX_Plates_Cam_9624_CineF44_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 144
    },
    "VFX_Plates_Cam_9624_CineF42_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 142
    },
    "A007C004_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 121
    },
    "A007C024_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 140
    },
    "A007C008_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 125
    },
    "A007C016_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 132
    },
    "A007C020_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 136
    },
    "VFX_Plates_Cam_9624_CineF45_FPS120": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 145
    },
    "A005C006_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 116
    },
    "A007C007_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 124
    },
    "A007C013_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 129
    },
    "A007C006_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 123
    },
    "VFX_Plates_Cam_9624_CineF62_FPS1000": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 1000,
        "isVisible": "",
        "startFrame": 1001,
        "id": 149
    },
    "VFX_Plates_Cam_9624_CineF46_FPS120": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 146
    },
    "A007C015_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 131
    },
    "A005C001_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 111
    },
    "A005C005_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 115
    },
    "A007C022_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 138
    },
    "A005C004_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 114
    },
    "VFX_Plates_Cam_9624_CineF48_FPS120": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 148
    },
    "A007C003_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 120
    },
    "A007C019_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 135
    },
    "VFX_Plates_Cam_9624_CineF43_FPS120": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 143
    },
    "A007C001_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 118
    },
    "A006C001_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 117
    },
    "A007C021_140914_FPS120": {
        "numOfFrames": 1001,
        "height": 1080,
        "width": 1920,
        "fps": 120,
        "isVisible": "",
        "startFrame": 1001,
        "id": 137
    }
  },
  "Smoke_and_Fog": {
    "A008C011_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 169
    },
    "A009C015_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 188
    },
    "A010C022_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 211
    },
    "A010C031_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 220
    },
    "A010C036_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 225
    },
    "A010C009_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 199
    },
    "A010C001_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 191
    },
    "A009C014_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 187
    },
    "A010C015_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 204
    },
    "A010C012_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 201
    },
    "A008C014_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 172
    },
    "A010C010_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 200
    },
    "A009C013_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 186
    },
    "A010C002_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 192
    },
    "A010C033_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 222
    },
    "A010C026_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 215
    },
    "A010C014_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 203
    },
    "A009C004_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 177
    },
    "A009C010_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 183
    },
    "A009C002_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 175
    },
    "A008C008_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 166
    },
    "A010C034_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 223
    },
    "A010C003_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 193
    },
    "A010C008_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 198
    },
    "A010C018_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 207
    },
    "A010C017_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 206
    },
    "A009C016_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 189
    },
    "A010C019_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 208
    },
    "A010C023_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 212
    },
    "A010C029_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 218
    },
    "A010C035_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 224
    },
    "A010C037_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 226
    },
    "A010C005_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 195
    },
    "A010C016_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 205
    },
    "A009C006_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 179
    },
    "A010C025_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 214
    },
    "A010C021_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 210
    },
    "A008C007_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 165
    },
    "A010C024_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 213
    },
    "A009C009_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 182
    },
    "A010C006_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 196
    },
    "A009C007_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 180
    },
    "A011C001_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 227
    },
    "A008C012_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 170
    },
    "A008C015_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 173
    },
    "A010C013_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 202
    },
    "A008C009_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 167
    },
    "A010C027_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 216
    },
    "A010C020_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 209
    },
    "A010C028_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 217
    },
    "A009C008_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 181
    },
    "A008C013_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 171
    },
    "A009C017_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 190
    },
    "A009C003_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 176
    },
    "A009C011_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 184
    },
    "A009C012_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 185
    },
    "A011C002_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 228
    },
    "A009C001_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 174
    },
    "A010C032_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 221
    },
    "A008C010_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 168
    },
    "A009C005_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 178
    },
    "A010C030_140914_FPS25": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 25,
        "isVisible": "",
        "startFrame": 1001,
        "id": 219
    },
    "A010C004_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 194
    },
    "A010C007_140914_FPS60": {
        "numOfFrames": 1001,
        "height": 1152,
        "width": 2048,
        "fps": 60,
        "isVisible": "",
        "startFrame": 1001,
        "id": 197
    }
  }
}

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
