import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
##https://github.com/LLNL/boxfish/blob/master/boxfish/GUIUtils.py
class myLabel(QtGui.QWidget):
	def __init__(self, parent=None):
		super(myLabel, self).__init__(parent=parent)
		self.text = "wvisssss"

	def mouseMoveEvent(self, e):
		drag = QtGui.QDrag(self)
		mimeData = QtCore.QMimeData()
		drag.setMimeData(mimeData)

		drag.setPixmap(QtGui.QPixmap.fromImage(self.createPixmap()))
		dropAction = drag.start(QtCore.Qt.MoveAction)


	def dragEnterEvent(self, e):
		print "drag me"


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



def main():
    
    app = QtGui.QApplication(sys.argv)
    w = myLabel()
    w.resize(250, 150)
    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()