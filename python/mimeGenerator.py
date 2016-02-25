
import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject, pyqtSignal
from browserViewerItem import ThumbnailItem, BrowserViewerItem
import settings

from PyQt4.QtCore import pyqtSignal, QSize, Qt
from PyQt4.QtGui import *

class MimeGenerator(QObject):
    signalItemDragged = pyqtSignal(str, name='itemDragged')
    def __init__(self, parent):
        super(MimeGenerator, self).__init__(parent=parent)
        self.parent = parent
        self.signalItemDragged.connect(self.itemDragged)
        self.text = "lol"
        pass


    def itemDragged(self, itemID ):
    	self.metaData =  settings.pathCache[settings.currentCategory][str(itemID)]

        #print settings.pathCache[self.parent.currentCategory][str(itemID)]
        drag = QtGui.QDrag(self.parent)
        mimeData = QtCore.QMimeData()
        mimeData.setText(self.generateNukeTCL())
        drag.setMimeData(mimeData)

        drag.setPixmap(QtGui.QPixmap.fromImage(self.createPixmap()))
        if drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
            print 'moved'
        else:
            print 'copied'


    def generateNukeTCL(self):
        command = ""
        command += """Read {{
            inputs 0
            file C:/Users/PC/Desktop/Projects/Elementsbrowser/ElementsBrowserPY/python/Categories/Cloth/A002C002_140913_FPS120/Thumbnails/A002C002_140913_FPS120.####.jpg
            origfirst {startFrame}
            origlast {startFrame} + {numOfFrames}
            first {startFrame}
            label Elementsbrowser ID # {id}
            }}""".format(**self.metaData)
        return command


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


# m = MimeGenerator()
# print m.generateNukeTCL()
# QString Thumbnail::generateNukeTCL(){

#     return QString("Read {inputs 0 file " + this->pathToSource + "" + this->fileName + ".####.exr" + "\n" +
#                    " proxy " + this->pathToProxy + this->fileName+ ".####.jpg"+               "\n" +
#                     "format " + "\"" + QString::number(this->imageWidth) + " " + QString::number(this->imageHeight) + "\""+               "\n" +
#                    " proxy_format " + "\"" + QString::number(this->imageWidth) + " " + QString::number(this->imageHeight) + "\""+               "\n" +
#                    " first " + QString::number(this->startFrame) + "\n" +
#                    " last  " + QString::number(this->startFrame + this->NumOfFrames -1)+ "\n" +
#                    " origfirst " + QString::number(this->startFrame) + "\n" +
#                    " origlast  " + (QString::number(this->startFrame + this->NumOfFrames-1))+ "\n" +
#                    " label " + "\"Elementsbrowser Id #" +  QString::number(this->Id)+ "\"" + "\n" +


#                    "}" );

# }
