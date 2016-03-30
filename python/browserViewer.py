#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject, pyqtSignal
from browserViewerItem import ThumbnailItem, BrowserViewerItem
import settings

from PyQt4.QtCore import pyqtSignal, QSize, Qt
from PyQt4.QtGui import *
from browserCategories import BrowserCategories
from mimeGenerator import MimeGenerator

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
        # note: using scrubFrame.zfill is logically incorrect, since the frame numbers
        #       on thhumbnails go to 50 while frame numbers on real footage go from
        #       startFrame to startFrame + numOfFrames
        #       to get the source file number corresponding ot a thumb:
        #       startFrame + (scrubFrame / float(50)) * numOfFrames

        # right now, we just open the folder instead, which loads all frames

        # constructPath = settings.sourcePath(settings.currentCategory, fileName)
        # self.openPathEXR = constructPath.replace('####', scrubFrame.zfill(4))
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



class BrowserViewer(QtGui.QListWidget):

    categoryChanged = pyqtSignal(str, name='categoryChanged')
    signalItemDragged = pyqtSignal(str, name='itemDragged')


    def __init__(self, parent):
        self.parent = parent
        super(BrowserViewer, self).__init__(parent)
        self.currentCategory = settings.showConfig["startCategory"]
        self.initUI()
        self.menu = ThumbContextMenu()

        self.mimeGenerator = MimeGenerator(self)
        self.categoryChanged.connect(self.changeCategory)
        self.signalItemDragged.connect(self.mimeGenerator.signalItemDragged)

        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        # self.customContextMenuRequested.connect(self.openMenu)


    def changeCategory(self, item):
        self.currentCategory = str(item)
        settings.currentCategory = self.currentCategory #todo make it less locally dependend,
        #as this one is called from the browserViewerItems
        self.populateWidgets(settings.pathCache[self.currentCategory])


    def initUI(self):
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.itemSelectionChanged.connect(self.selectedItems)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)



        self.setViewMode(QtGui.QListView.IconMode)
        self.setResizeMode(QtGui.QListView.Adjust)


        self.itemHolder = []

        #Initialize Empty Thumbnails
        for pos in range(0, settings.thumbnails["numOfThumbnails"]):
            item = QtGui.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(settings.thumbnails["width"], settings.thumbnails["height"]))
            self.insertItem(pos, item)
            previewWindow = BrowserViewerItem(self, "None")
            self.itemHolder.append(previewWindow)
            self.setItemWidget(item, previewWindow)


        self.populateWidgets(settings.pathCache[self.currentCategory])

        self.setWindowTitle(settings.about["name"])
        self.show()


    def selectedItems(self, event):
        print "waiting to be implemented: selectedItems"
        pass

    def mousePressEvent(self, e):
        print e.pos()


    def dragEnterEvent(self, e):
        print "dragging started."


    def populateWidgets(self, iterable):
        #print iterable
        for index, element in enumerate(iterable.keys()):
            #print element
            self.itemHolder[index].thumbnailItem.setData(element)
            self.itemHolder[index].setData(element)
            self.itemHolder[index].setActive(True)

        #If there are too many, override them with blank
        for index in range(len(iterable), settings.thumbnails["numOfThumbnails"]):
            self.itemHolder[index].setActive(False)



def main():
    #Only for Debugging Purposes
    #open mediaBrowser.py to start
    app = QtGui.QApplication(sys.argv)

    #Load Stye Sheet
    with open("../resources/style.qss", "r") as myfile:
        data = ' '.join([line.replace('\n', '') for line in myfile.readlines()])
    app.setStyleSheet(data)


    browserViewer = BrowserViewer(None)
    window = BrowserCategories()
    window.show()
    window.categoryChanged.connect(browserViewer.categoryChanged)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
