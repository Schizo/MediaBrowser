import sys
from PyQt4 import QtGui, QtCore

from browserViewer import BrowserViewer
from browserViewer import BrowserCategories
from sequenceAdder import SequenceAdder
from PyQt4.QtCore import QTimer, Qt


class ElementsBrowser(QtGui.QTabWidget):
    def __init__(self):
        super(ElementsBrowser, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowState(QtCore.Qt.WindowActive)
        browserCategories = BrowserCategories()
        browserCategories.setMinimumWidth(200)
        browserViewer = BrowserViewer(self)
        browserCategories.categoryChanged.connect(
            browserViewer.categoryChanged)

        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(browserCategories)
        splitter.addWidget(browserViewer)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([200, 400])

        sequenceAdder = SequenceAdder(self)

        self.addTab(splitter, "Browse")
        self.addTab(sequenceAdder, "Add Elements")

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        self.setWindowTitle('ElementsBrowser')
        self.show()
        #Make sure window starts at front
        self.raise_()

    def mousePressEvent(self, event):
        print event.pos()


def main():
    app = QtGui.QApplication(sys.argv)

    # Load Stye Sheet
    with open("../resources/style.qss", "r") as myfile:
        data = ' '.join([line.replace('\n', '')
                         for line in myfile.readlines()])
    app.setStyleSheet(data)


    ex = ElementsBrowser()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
