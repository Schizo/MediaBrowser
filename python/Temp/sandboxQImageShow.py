#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows an icon
in the titlebar of the window.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
import os
from PyQt4 import QtGui, QtCore

class ImageWidget(QtGui.QLabel):
    """docstring for ImageWidget"""
    def __init__(self, parent, filepath=None):
        super(ImageWidget, self).__init__(parent=parent)
        self.currentDirectory, self.fileName = os.path.split(filepath)
        #self.currentDirectory = "/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Blood/VFX_Plates_Cam_9624_CineF27_FPS1000/Thumbnails/"
        #self.fileName = "VFX_Plates_Cam_9624_CineF27_FPS1000.0001.jpg"
        self.pixmap = QtGui.QPixmap(self.currentDirectory + "/" + self.fileName)
        self.setPixmap(self.pixmap)
        self.setMouseTracking(True)
        self.setMinimumHeight(100)
        
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)

    def mouseMoveEvent(self, event):
        currentFrame =  str(event.x()/4)

        splitted =  self.fileName.split(".")
        splitted[1] = currentFrame.zfill(4)

        self.fileName = ".".join(splitted)

        newPath = self.currentDirectory + "/" + self.fileName
        self.pixmap = QtGui.QPixmap(newPath)
        
        self.setPixmap(self.pixmap)
        print newPath
        

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        

        pathlist = ['/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C001_140913_FPS120/Thumbnails/A002C001_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C002_140913_FPS120/Thumbnails/A002C002_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C003_140913_FPS120/Thumbnails/A002C003_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C004_140913_FPS120/Thumbnails/A002C004_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C005_140913_FPS120/Thumbnails/A002C005_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C006_140913_FPS120/Thumbnails/A002C006_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C007_140913_FPS120/Thumbnails/A002C007_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C008_140913_FPS120/Thumbnails/A002C008_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C009_140913_FPS120/Thumbnails/A002C009_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C010_140913_FPS120/Thumbnails/A002C010_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C011_140913_FPS120/Thumbnails/A002C011_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C012_140913_FPS120/Thumbnails/A002C012_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C013_140913_FPS120/Thumbnails/A002C013_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C014_140913_FPS120/Thumbnails/A002C014_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C015_140913_FPS120/Thumbnails/A002C015_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C016_140913_FPS120/Thumbnails/A002C016_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C017_140913_FPS120/Thumbnails/A002C017_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C018_140913_FPS120/Thumbnails/A002C018_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C019_140913_FPS120/Thumbnails/A002C019_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C020_140913_FPS120/Thumbnails/A002C020_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C021_140913_FPS120/Thumbnails/A002C021_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C022_140913_FPS120/Thumbnails/A002C022_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C023_140913_FPS120/Thumbnails/A002C023_140913_FPS120.0001.jpg', '/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Cloth/A002C024_140913_FPS120/Thumbnails/A002C024_140913_FPS120.0001.jpg']

        widget = QtGui.QListWidget(self)
        widget.setMinimumWidth(1024)
        widget.setMinimumHeight(1024)
        
        
        
        #w = ImageWidget(widget, pathlist[0])
        


        
        #print pathlist[0]
        #widget.setItemWidget(image, widget)

        # mywidget = QtGui.QTableWidget(self)
        # mywidget.setColumnCount(5)
        # mywidget.setRowCount(5)
        # mywidget.resizeRowsToContents()
        # mywidget.resizeColumnsToContents()
        # mywidget.setMinimumWidth(1024)
        # mywidget.setMinimumHeight(1024)
        # mywidget.horizontalHeader().setVisible(False)
        # mywidget.verticalHeader().setVisible(False)

        #Populate random
        for x in range(0, 5):
            #mywidget.setColumnWidth(x, 200)
            #mywidget.setRowHeight(x, 120)
            for y in range(0, 5):
                #image = ImageWidget(mywidget)
                #print id(image)
                #mywidget.setCellWidget(x, y, ImageWidget(mywidget, pathlist[x*y]))
                item = QtGui.QListWidgetItem()
                widget.insertItem(x*y, item)
                widget.setItemWidget(item, ImageWidget(widget, pathlist[x*y]))

        
        self.setGeometry(300, 300, 1024, 1024)
        self.setWindowTitle('Icon')
    
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    