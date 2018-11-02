from __future__ import division

from PySide2 import QtCore, QtGui, QtWidgets
# noinspection PyUnresolvedReferences
from rcc_bundles import bundle_pyside2


class Window90Degree(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window90Degree, self).__init__(parent=parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self._dpi = self.logicalDpiX() / 96

        print(self._dpi)

        self.corner_radius = 10 * self._dpi

        self.px_background = QtGui.QPixmap(":/background.png")
        self.px_close = QtGui.QPixmap(":/close.png")
        self.px_left = QtGui.QPixmap(":/left.png")
        self.px_right = QtGui.QPixmap(":/right.png")
        self.px_title = QtGui.QPixmap(":/title.png")
        self.px_x = QtGui.QPixmap(":/x.png")
        self.px_y = QtGui.QPixmap(":/y.png")
        self.px_z = QtGui.QPixmap(":/z.png")

        self.rect_close = QtCore.QRect((self.width() - (self.px_close.width() // 2 * self._dpi)),
                                       0,
                                       self.px_close.width() // 2 * self._dpi,
                                       self.px_close.height() // 2 * self._dpi)

        self.rect_title = QtCore.QRect((self.width() - (self.px_title.width() // 2 * self._dpi)) / 2,
                                       15 * self._dpi,
                                       self.px_title.width() // 2 * self._dpi,
                                       self.px_title.height() // 2 * self._dpi)

        self.rect_left = QtCore.QRect(0,
                                      230 / 2 * self._dpi,
                                      self.px_left.width() // 2 * self._dpi,
                                      self.px_left.height() // 2 * self._dpi)

        self.rect_right = QtCore.QRect(self.width() - (self.px_right.width() // 2 * self._dpi),
                                       230 / 2 * self._dpi,
                                      self.px_left.width() // 2 * self._dpi,
                                       self.px_right.height() // 2 * self._dpi)
        print(self.width())
        print(self.size())
        print(self.rect_close)

        self.brush_white = QtGui.QBrush(QtCore.Qt.white)
        self.brush_red = QtGui.QBrush(QtCore.Qt.red)
        self.brush_green = QtGui.QBrush(QtCore.Qt.green)
        self.brush_blue = QtGui.QBrush(QtCore.Qt.blue)

    def sizeHint(self):
        width = (self.px_background.size().width() // 2) * self._dpi
        height = (self.px_background.size().height() // 2) * self._dpi
        size = QtCore.QSize(width, height)
        return size

    def width(self):
        return self.size().width()

    def height(self):
        return self.size().height()

    def size(self):
        """ actual widget size """
        return self.sizeHint()

    def rect(self):
        """ rect for the entire widget """
        return QtCore.QRect(0, 0, self.width(), self.height())

    def paintEvent(self, event):
        """ widget painting happens here """
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)

        self._do_paint(painter)

        painter.end()

        event.accept()

    def _do_paint(self, painter):
        """ actual paint ops """
        path = QtGui.QPainterPath()
        path.addRoundedRect(self.rect(), self.corner_radius, self.corner_radius)

        # painter.setClipPath(path, QtCore.Qt.ReplaceClip)

        painter.fillPath(path, self.brush_white)

        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceAtop)
        painter.drawPixmap(self.rect(),
                           self.px_background)

        painter.drawPixmap(self.rect_title,
                           self.px_title)

        painter.drawPixmap(self.rect_close,
                           self.px_close)

        painter.drawPixmap(self.rect_left,
                           self.px_left)
        painter.drawPixmap(self.rect_left.adjusted(0, self.rect_left.height(),
                                                   0, self.rect_left.height()),
                           self.px_left)
        painter.drawPixmap(self.rect_left.adjusted(0, self.rect_left.height() * 2,
                                                   0, self.rect_left.height() * 2),
                           self.px_left)

        painter.drawPixmap(self.rect_right,
                           self.px_right)
        painter.drawPixmap(self.rect_right.adjusted(0, self.rect_right.height(),
                                                   0, self.rect_right.height()),
                           self.px_right)
        painter.drawPixmap(self.rect_right.adjusted(0, self.rect_right.height() * 2,
                                                   0, self.rect_right.height() * 2),
                           self.px_right)


def load():
    """
    entry point for the UI, launch an instance of the tool with this method
    """
    global _win
    try:
        _win.close()
    except (NameError, RuntimeError):
        pass
    finally:
        _win = Window90Degree()
        _win.show()
