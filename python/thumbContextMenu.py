from PyQt4 import QtGui, QtCore
import settings
import os
import subprocess

class ThumbContextMenu(QtGui.QMenu):
    def __init__(self):
        super(ThumbContextMenu, self).__init__()

        # disabled, since it has been broken in the old ElementsBrowser for a few months and no one complained
        # self.addAction("Open EXR Photoshop", self.openPhotoshopEXR)
        # self.addAction("Open JPG Photoshop", self.openPhotoshopJPG)

        self.addAction("Open EXR in RV", self.openRVEXR)
        self.addAction("Open JPG in RV", self.openRVJPG)
        # self.addAction("Open EXR in djv", self.openDJVEXR)
        # self.addAction("Open JPG in djv", self.openDJVJPG)
        self.addAction("Open Folder Location", self.openFolder)
        self.addAction("Remove from DB", self.removeFromDB)

    def setFileData(self, scrubFrame, fileName):
        """Sets the Path to a file directory"""
        self.openPathEXR = constructPath.replace('####', scrubFrame.zfill(4))
        self.fileName = fileName

        self.openPathEXR = os.path.split(settings.sourcePath(settings.currentCategory, fileName))[0]
        self.openPathJPG = os.path.split(settings.proxyPath(settings.currentCategory, fileName))[0]

        self.locationPath = settings.locationPath(settings.currentCategory, fileName)

    # def openPhotoshopEXR(self):
    #     print "opening Photoshop"
    #     print self.openPathEXR
    #
    # def openPhotoshopEXR(self):
    #     print "opening Photoshop"
    #     print self.openPathJPG

    def openRVEXR(self):
        # print "opening RV"
        # print "rv: " + settings.appPath["rv"]
        # print self.openPathEXR
        subprocess.Popen([settings.appPath["rv"], self.openPathEXR])

    def openRVJPG(self):
        print "opening RV"
        subprocess.Popen([settings.appPath["rv"], self.openPathJPG])

    # def openDJVEXR(self):
    #     os.system(settings.appPath["djv"] + " " + self.openPathEXR)
    #     # subprocess.Popen([settings.appPath["djv"], self.openPathEXR])
    #
    # def openDJVJPG(self):
    #     subprocess.Popen([settings.appPath["djv"], self.openPathJPG + "/*"])

    def openFolder(self):
        subprocess.Popen([settings.appPath["explorer"], self.locationPath.replace("/","\\")])

    def removeFromDB(self):
        settings.removeItem(settings.currentCategory, self.fileName)
