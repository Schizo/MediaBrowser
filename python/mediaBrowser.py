import sys
from PyQt4 import QtGui, QtCore

from browserViewer import BrowserViewer
from browserViewer import BrowserCategories

class ElementsBrowser(QtGui.QTabWidget):
    def __init__(self):
        super(ElementsBrowser, self).__init__()
        self.initUI()

    def initUI(self):

        #Todo: Add Vertical Spliter for
        hbox = QtGui.QHBoxLayout(self)
        browserCategories = BrowserCategories()
        browserCategories.setMinimumWidth(200)
       
        browserViewer = BrowserViewer(self)
        browserCategories.categoryChanged.connect(browserViewer.categoryChanged)

        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(browserCategories)
        splitter.addWidget(browserViewer)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([200, 400])
        self.setMinimumWidth(840)
        self.setMinimumHeight(840)
        
        hbox.addWidget(splitter)
        btn = QtGui.QPushButton("test")

        self.addTab(splitter, "Browse")
        self.addTab(btn, "Manage Elements")
            

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        self.setWindowTitle('ElementsBrowser')
        self.show()
        

    def mousePressEvent(self, event):
        print event.pos()

def main():
    app = QtGui.QApplication(sys.argv)
    #Load Stye Sheet
    with open("../resources/style.qss", "r") as myfile:
        data = ' '.join([line.replace('\n', '') for line in myfile.readlines()])
    app.setStyleSheet(data)

    ex = ElementsBrowser()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()  