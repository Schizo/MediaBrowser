import sys
from PyQt4 import QtGui, QtCore

from browserViewer import BrowserViewer
from browserViewer import BrowserCategories

class ElementsBrowser(QtGui.QWidget):
    def __init__(self):
        super(ElementsBrowser, self).__init__()
        self.initUI()

    def initUI(self):

        #Todo: Add Vertical Spliter for
        hbox = QtGui.QHBoxLayout(self)
        browserCategories = BrowserCategories()
       
        browserViewer = BrowserViewer(self)#QtGui.QWidget(self)
        btn = QtGui.QPushButton("test")
        browserCategories.categoryChanged.connect(browserViewer.categoryChanged)

        
        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(browserCategories)
        splitter.addWidget(browserViewer)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([125, 150])
        
        hbox.addWidget(splitter)
        self.setLayout(hbox)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        self.setGeometry(300, 300, 1160, 600)
        self.setWindowTitle('QtGui.QSplitter')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    #Load Stye Sheet
    with open("../ressources/style.qss", "r") as myfile:
        data = ' '.join([line.replace('\n', '') for line in myfile.readlines()])
    app.setStyleSheet(data)

    ex = ElementsBrowser()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()  