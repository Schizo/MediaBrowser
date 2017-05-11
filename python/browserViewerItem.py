import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4.QtGui import *
import settings


class ThumbnailItem(QtGui.QLabel):
    """Represents an Elemement within a view, contains an Image and TextFields"""
    signalItemDragged = pyqtSignal(str, name='itemDragged')
    #menu = ThumbContextMenu() 


    def __init__(self, parent, filepath=None):
        super(ThumbnailItem, self).__init__(parent=parent)
        self.setData(filepath)
        self.setAcceptDrops(True)
        self.signalItemDragged.connect(parent.signalItemDragged)

        self.text = "empty text"
        self.key = ""
    

    def setData(self, fileName):
        self.fileName = fileName

        head, self.fileName = os.path.split(fileName)

        self.dirPath = settings.thumbPath(settings.currentCategory, fileName)
        self.composedPath =  self.dirPath + self.fileName +  ".0001.jpg"
        
        self.pixmap = QtGui.QPixmap(self.composedPath)
        self.setPixmap(self.pixmap)

        self.setMouseTracking(True)



    #This hole block should be part of the overall Viewer
    #As we build this object for every Element
    #which is consuming ressources

    def mouseMoveEvent(self, event):
        currentFrame =  str(max(event.x()/4, 1)) 
        self.scrubValue = currentFrame.zfill(4)
        self.currentThumbFile = self.fileName + "." + self.scrubValue + ".jpg"

        newPath = os.path.join(self.dirPath, self.currentThumbFile)
        self.pixmap = QtGui.QPixmap(newPath)
        
        self.setPixmap(self.pixmap)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.signalItemDragged.emit(self.fileName)
        elif event.button() == QtCore.Qt.RightButton:
            parentPosition = self.mapToGlobal(event.pos())
            self.parent().parent.menu.setFileData(self.scrubValue, self.fileName)
            self.parent().parent.menu.move(parentPosition)
            self.parent().parent.menu.show()

    def createPixmap(self):
        """Creates the pixmap shown when this label is dragged."""
        font_metric = QtGui.QFontMetrics(QtGui.QFont())
        text_size = font_metric.size(QtCore.Qt.TextSingleLine, self.text)
        image = QtGui.QImage(text_size.width() + 4, text_size.height() + 4,
            QtGui.QImage.Format_ARGB32_Premultiplied)
        image.fill(QtGui.qRgba(240, 140, 120, 255))

        painter = QtGui.QPainter()
        painter.begin(image)
        painter.setFont(QtGui.QFont())
        painter.setBrush(QtCore.Qt.black)
        painter.drawText(QtCore.QRect(QtCore.QPoint(2, 2), text_size), QtCore.Qt.AlignCenter,
            self.text)
        painter.end()
        return image

class BrowserViewerItem(QtGui.QWidget):
    def __init__(self, parent, filepath=None):
        super(BrowserViewerItem, self).__init__(parent=parent)
        self.setObjectName("thumbnail")
        self.parent = parent

        #init layout
        self.widgetsLayout = QtGui.QVBoxLayout()
        self.widgetsLayout.setSpacing(0)
        contentsMargin = 1
       
        self.widgetsLayout.setContentsMargins(contentsMargin, contentsMargin, contentsMargin, contentsMargin)
        self.thumbnailItem = ThumbnailItem(parent, filepath)
       
        #top Meta
        self.topWidget = QtGui.QLabel()
        self.topWidget.setObjectName("topWidget")
        self.topLayout = QtGui.QHBoxLayout()
        self.topLayout.setSpacing(0)
        contentsMargin = 0
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


    #todo, better string formatting
    def setData(self, fileName):
        self.numOfFrames = settings.pathCache[settings.currentCategory][fileName]["numOfFrames"]
        self.height      = settings.pathCache[settings.currentCategory][fileName]["height"]
        self.width       = settings.pathCache[settings.currentCategory][fileName]["width"]
        self.fps         = settings.pathCache[settings.currentCategory][fileName]["fps"]
        self.startFrame  = settings.pathCache[settings.currentCategory][fileName]["startFrame"]
        self.index      = settings.pathCache[settings.currentCategory][fileName]["id"]

        self.frameInfo.setText(str(self.numOfFrames) + " @ " + str(self.fps) + " fps")
        self.id.setText("# " + str(self.index))

