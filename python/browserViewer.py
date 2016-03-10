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

class ThumbContextMenu(QtGui.QMenu):
    def __init__(self):
        super(ThumbContextMenu, self).__init__()
        self.addAction("Open EXR Photoshop", self.openPhotoshop)
        self.addAction("Open JPG Photoshop", self.openPhotoshop)
        self.addAction("Open EXR in RV", self.openRV)
        self.addAction("Open JPG in RV", self.openRV)
        self.addAction("Open Folder Location", self.openFolder)
        self.addAction("Remove from DB")

    def setFileData(self, scrubFrame, fileName):
        constructPath = settings.sourcePath(settings.currentCategory, fileName)
        self.openPath = constructPath.replace('####', scrubFrame.zfill(4))


    def openPhotoshop(self):
        print "opening Photoshop"
        print self.openPath

    def openRV(self):
        print "opening RV"

    def openFolder(self):
        print "opening Folder"



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
        self.customContextMenuRequested.connect(self.openMenu)


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