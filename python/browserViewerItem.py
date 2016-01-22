import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject, pyqtSignal


class ThumbnailItem(QtGui.QLabel):
    """Represents an Elemement within a view, contains an Image and TextFields"""
    def __init__(self, parent, filepath=None):
        super(ThumbnailItem, self).__init__(parent=parent)
        self.setData(filepath)


    def setData(self, filepath):
        self.rootPath = "Categories/"
        head, self.fileName = os.path.split(filepath)

        self.dirPath = self.rootPath + filepath + "/Thumbnails/"
        self.composedPath =  self.dirPath + self.fileName +  ".0001.jpg"
        
        self.pixmap = QtGui.QPixmap(self.composedPath)
        self.setPixmap(self.pixmap)

        self.setMouseTracking(True)

    #This hole block should be part of the overall Viewer
    #As we build this object for every Element
    #which is consuming ressources
    def mousePressEvent(self, event):
        position = event.globalPos()
        # self.mapper = QtCore.QSignalMapper(self)

        # for text in 'One Two Three'.split():
        #     action = QtGui.QAction(text, self)
        #     self.mapper.setMapping(action, text)
        #     action.triggered.connect(self.mapper.map)
        #     self.toolbar.addAction(action)

        # if event.button() == QtCore.Qt.RightButton:
        #     menu = QtGui.QMenu()
        #     menu.addAction(self.tr("Edit person"))
        #     menu.addAction(self.tr("Edit person"))
        #     menu.addAction(self.tr("Edit person"))
        #     menu.addAction(self.tr("Edit person"))
        #     menu.addAction(self.tr("Edit person"))
        #     menu.exec_(position)


    def mouseMoveEvent(self, event):
        currentFrame =  str(max(event.x()/4, 1)) 
        self.scrubValue = currentFrame.zfill(4)
        self.currentThumbFile = self.fileName + "." + self.scrubValue + ".jpg"

        newPath = os.path.join(self.dirPath, self.currentThumbFile)
        self.pixmap = QtGui.QPixmap(newPath)
        
        self.setPixmap(self.pixmap)


class BrowserViewerItem(QtGui.QLabel):
    def __init__(self, parent, filepath=None):
        super(BrowserViewerItem, self).__init__(parent=parent)
        self.setObjectName("thumbnail")
        #init layout
        self.widgetsLayout = QtGui.QVBoxLayout()
        self.widgetsLayout.setSpacing(0)
        self.widgetsLayout.setContentsMargins(5, 5, 5, 5)
        self.thumbnailItem = ThumbnailItem(parent, filepath)

        #top Meta
        self.topWidget = QtGui.QLabel()
        self.topWidget.setObjectName("topWidget")
        self.topLayout = QtGui.QHBoxLayout()
        self.topLayout.setSpacing(0)
        self.topLayout.setContentsMargins(1, 1, 1, 1)

        

        self.topWidget.setLayout(self.topLayout)

        self.id = QtGui.QLabel("# Id")
        self.id.setObjectName("metaFileID")
        self.id.setAlignment(QtCore.Qt.AlignLeft)


        self.favorite = QtGui.QCheckBox("")
        self.favorite.setObjectName("Favorite")
        self.favorite.setLayoutDirection(QtCore.Qt.RightToLeft)

        self.topLayout.addWidget(self.id)
        self.topLayout.addWidget(self.favorite)

        #Body Meta
        self.widgetsLayout.addWidget(self.topWidget)
        self.widgetsLayout.addWidget(self.thumbnailItem)
        
        #Bottom Meta
        self.bottomWidget = QtGui.QLabel()
        self.bottomLayout = QtGui.QHBoxLayout()
        self.bottomLayout.setSpacing(0)
        self.bottomLayout.setContentsMargins(1, 1, 1, 1)
        self.bottomWidget.setLayout(self.bottomLayout)

        self.resolution = QtGui.QLabel("HD")
        self.resolution.setObjectName("metaResolution")        
        self.frameInfo = QtGui.QLabel("#13 Frames @ 60fps")
        self.frameInfo.setObjectName("metaFpsFrames")
        self.frameInfo.setAlignment(QtCore.Qt.AlignLeft)
        self.resolution.setAlignment(QtCore.Qt.AlignRight)
        self.bottomLayout.addWidget(self.frameInfo)
        self.bottomLayout.addWidget(self.resolution)
        self.widgetsLayout.addWidget(self.bottomWidget)
        self.setLayout(self.widgetsLayout)

        #Make Childs invisible
        self.topWidget.setVisible(False)
        self.bottomWidget.setVisible(False)

    def setActive(self, isActive):
        #Refactor this, there is a bug, theoretically
        #Hiding the Parent would hide the children
        if isActive:
            self.setVisible(True)
            self.topWidget.setVisible(True)
            self.bottomWidget.setVisible(True)
        else:
            pass
            self.setVisible(False)
            self.topWidget.setVisible(False)
            self.bottomWidget.setVisible(False)


