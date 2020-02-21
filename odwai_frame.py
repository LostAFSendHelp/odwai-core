import sys
import tkinter as tk

from PyQt5 import QtWidgets, QtCore, QtGui

class CustomFrame(QtWidgets.QWidget):
    def __init__(self, point1, point2):
        super().__init__()
        root = tk.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        
        self.setGeometry(0, 0, width, height)
        self.setWindowTitle("Custom frame")
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(.3)
        self.is_snipping = False
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.point1 = { "x": point1["x"], "y": point2["x"] }
        self.point2 = { "x": point1["x"], "y": point2["x"] }

        self.show()

    def paintEvent(self, event):
        brush_color = (128, 128, 128, 128)
        line_width = 1

        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor("black"), line_width))
        qp.setBrush(QtGui.QColor(*brush_color))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_X:
            self.point1["x"] = self.begin.x()
            self.point1["y"] = self.begin.y()
            self.point2["x"] = self.end.x()
            self.point2["y"] = self.end.y()
            self.close()
        event.accept()

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        pass
        
