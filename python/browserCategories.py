from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal, QSize, Qt
import settings


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
