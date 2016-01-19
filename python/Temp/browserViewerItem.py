import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject, pyqtSignal


class ThumbnailItem(QtGui.QLabel):
    """Represents an Elemement within a view, contains an Image and TextFields"""
    def __init__(self, parent, filepath=None):
        super(ThumbnailItem, self).__init__(parent=parent)
        self.setData(filepath)


    def setData(self, filepath):
        self.rootPath = "/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/"
        head, self.fileName = os.path.split(filepath)

        self.dirPath = self.rootPath + filepath + "/Thumbnails/"
        self.composedPath =  self.dirPath + self.fileName +  ".0001.jpg"
        

        self.pixmap = QtGui.QPixmap(self.composedPath)
        self.setPixmap(self.pixmap)

        self.setMouseTracking(True)


    def setActive(self, isActive):
        if isActive:
            self.setMouseTracking(True)
        else:
            self.setMouseTracking(False)
            self.setData("None")



    def mouseMoveEvent(self, event):
        currentFrame =  str(max(event.x()/4, 1)) 


        self.scrubValue = currentFrame.zfill(4)
        self.currentThumbFile = self.fileName + "." + self.scrubValue + ".jpg"

        newPath = os.path.join(self.dirPath, self.currentThumbFile)
        self.pixmap = QtGui.QPixmap(newPath)
        
        self.setPixmap(self.pixmap)


class BrowserViewerItem(QtGui.QWidget):
    def __init__(self, parent, filepath=None):
        super(BrowserViewerItem, self).__init__(parent=parent)
        self.innerLayout = QtGui.QVBoxLayout()
        self.thumbnailItem = ThumbnailItem(parent, filepath)

        vbox = QtGui.QVBoxLayout(self.thumbnailItem)
        self.metaInfo = QtGui.QLabel("fisiki")
        self.metaInfo.setObjectName("fps")
        self.metaInfo.setAlignment(QtCore.Qt.AlignLeft)
        vbox.addWidget(self.metaInfo)

        self.innerLayout.addWidget(self.thumbnailItem)
        self.setLayout(self.innerLayout)



