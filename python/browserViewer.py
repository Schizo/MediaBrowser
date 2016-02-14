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
       



class BrowserCategories(QtGui.QWidget):
    categoryChanged = pyqtSignal(str, name='categoryChanged')
    def __init__(self):
        
    
        QtGui.QWidget.__init__(self)
        
        self.treeView = QtGui.QTreeView()
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)
        self.treeView.clicked.connect(self.clicked)
        
        self.model = QtGui.QStandardItemModel()
        self.addItems(self.model, settings.data)
        self.treeView.setModel(self.model)
        
        self.model.setHorizontalHeaderLabels([self.tr("Object")])
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.treeView)
        self.setLayout(layout)
    
    def addItems(self, parent, elements):
        for text, children in elements:
            item = QtGui.QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.addItems(item, children)

    def clicked(self, index):
        parentsList = []
        self.traverseUp(index, parentsList)
        parentsList.reverse()
        selectedItem = str(index.data().toString())
        path = ''.join(parentsList)

        #Build up path, if element is a child of a Category
        if path:
            self.categoryChanged.emit(path + "/" + selectedItem)
        else:
            self.categoryChanged.emit(selectedItem)


    def traverseUp(self, item, parentsList):
        hasParents = True
        itemData = item.parent().data().toString()
        if itemData:
            parentsList.append(str(itemData))
            self.traverseUp(item.parent(), parentsList)

    def openMenu(self, position):
        print position
    
        indexes = self.treeView.selectedIndexes()
        if len(indexes) > 0:
        
            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level += 1
        
        menu = QMenu()
        if level == 0:
            menu.addAction(self.tr("Edit person"))
        elif level == 1:
            menu.addAction(self.tr("Edit object/container"))
        elif level == 2:
            menu.addAction(self.tr("Edit object"))
        
        menu.exec_(self.treeView.viewport().mapToGlobal(position))


class BrowserViewer(QtGui.QListWidget):
    
    categoryChanged = pyqtSignal(str, name='categoryChanged')
    

    def __init__(self, parent):
        self.parent = parent
        super(BrowserViewer, self).__init__(parent)
        self.initUI()
        self.categoryChanged.connect(self.changeCategory)
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu )
        self.customContextMenuRequested.connect(self.openMenu)

    def changeCategory(self, item):
        self.populateWidgets(settings.pathCache[str(item)])

   
    def initUI(self):

        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.itemSelectionChanged.connect(self.selectedItems)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)

        quitAction = QAction("Quit", self)
        quitAction.triggered.connect(qApp.quit)
        self.addAction(quitAction)

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



        #self.setGeometry(300, 300, 1024, 1024)
        self.populateWidgets(settings.pathCache['Fire/Flames'])

        self.setWindowTitle(settings.about["name"])
        self.show()


    def openMenu(self):
        print "openMenu"

    def selectedItems(self):
        print "waiting to be implemented"
        pass

    def dragEnterEvent(self, e):
        print "dragging started."

    def populateWidgets(self, iterable):
        print len(iterable)
        for index, path in enumerate(iterable):
            self.itemHolder[index].thumbnailItem.setData(path)
            self.itemHolder[index].setActive(True)

        #If there are too many, override them with blank
        for index in range(len(iterable), settings.thumbnails["numOfThumbnails"]):
            self.itemHolder[index].setActive(False)



def main():
    #Only for Debugging Purposes
    #open mediaBrowser.py to start
    app = QtGui.QApplication(sys.argv)

    #Load Stye Sheet
    with open("../ressources/style.qss", "r") as myfile:
        data = ' '.join([line.replace('\n', '') for line in myfile.readlines()])
    app.setStyleSheet(data)


    browserViewer = BrowserViewer(None)
    window = BrowserCategories()
    window.show()
    window.categoryChanged.connect(browserViewer.categoryChanged)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    