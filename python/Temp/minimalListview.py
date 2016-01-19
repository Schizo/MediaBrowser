import sys
import os

from PyQt4 import QtGui, QtCore

class imageView(QtCore.QObject):
    """docstring for imageView"""
    def __init__(self):
        pass

class MyListModel(QtCore.QAbstractListModel): 
    def __init__(self, datain, parent=None, *args): 
        """ datain: a list where each item is a row
        """
        QtCore.QAbstractListModel.__init__(self, parent, *args) 
        self.listdata = datain

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self.listdata) 

    def data(self, index, role):
        if index.isValid() and role == QtCore.Qt.DecorationRole:

            print index.row()
            pixmap = QtGui.QPixmap(self.listdata[index.row()])
            #print dir(pixmap)
            icon = QtGui.QIcon(pixmap)
            return icon


        if index.isValid() and role == QtCore.Qt.DisplayRole:
            #return QtCore.QVariant(os.path.splitext(os.path.split(self.listdata[index.row()])[-1])[0])
            return QtCore.QVariant("a")
        else: 
            return QtCore.QVariant()




        

class MyListView(QtGui.QListView):
    """docstring for MyListView"""
    def __init__(self):
        super(MyListView, self).__init__()
        # show in Icon Mode
        self.setViewMode(QtGui.QListView.IconMode)
        self.setResizeMode(QtGui.QListView.Adjust)
        self.setMouseTracking(True)

        self.setGridSize(QtCore.QSize(200, 112))
        self.setIconSize(QtCore.QSize(200, 112))

        currentDirectory = "/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/Blood/VFX_Plates_Cam_9624_CineF27_FPS1000/Thumbnails"
        # create table
        thumbPathes = []
        fileNames = os.listdir(currentDirectory)
        for fileName in fileNames:
            if fileName.endswith(".jpg"):
                thumbPathes.append(os.path.join(currentDirectory, fileName))
        lm = MyListModel(thumbPathes, self)
        self.setModel(lm)
        self.show()

    def mouseMoveEvent(self, event):
        print 'mouseMoveEvent: x=%d, y=%d' % (event.x(), event.y())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window =  MyListView()
    window.show()
    window.raise_()
    sys.exit(app.exec_())