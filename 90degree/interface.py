from __future__ import division

from PySide2 import QtCore, QtGui, QtWidgets
# noinspection PyUnresolvedReferences
from rcc_bundles import bundle_pyside2


class Window90Degree(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window90Degree, self).__init__(parent=parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)

        self._dpi = self.logicalDpiX() / 96

        print(self._dpi)
        self._enter_close = False
        self._enter_x_left = False
        self._enter_x_right = False
        self._enter_y_left = False
        self._enter_y_right = False
        self._enter_z_left = False
        self._enter_z_right = False

        self.corner_radius = 10 * self._dpi

        self.px_background = QtGui.QPixmap(":/background.png")
        self.px_close = QtGui.QPixmap(":/close.png")
        self.img_close = self.px_close.toImage()  # type: QtGui.QImage
        self.px_left = QtGui.QPixmap(":/left.png")
        self.px_right = QtGui.QPixmap(":/right.png")
        self.px_title = QtGui.QPixmap(":/title.png")
        self.px_x = QtGui.QPixmap(":/x.png")
        self.px_y = QtGui.QPixmap(":/y.png")
        self.px_z = QtGui.QPixmap(":/z.png")

        self.brush_white = QtGui.QBrush(QtCore.Qt.white)

        self.color_out_close = QtGui.QColor(255, 255, 255, 128)
        self.color_in_close = QtGui.QColor(255, 0, 0, 255)
        self.color_close = self.color_out_close

        self.color_faded = QtGui.QColor(255, 255, 255, 75)

        self.color_white = QtCore.Qt.white
        self.color_red = QtCore.Qt.red
        self.color_green = QtCore.Qt.green
        self.color_blue = QtCore.Qt.blue

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

        self.rect_center = QtCore.QRect(self.rect_left.topRight().x(),
                                        self.rect_left.topRight().y(),
                                        self.px_x.width() // 2 * self._dpi,
                                        self.px_x.height() // 2 * self._dpi)

        self.rect_x_left = QtCore.QRect(self.rect_left.topLeft(),
                                        QtCore.QPoint(self.width() // 2, self.rect_left.bottom()))
        self.rect_x_right = QtCore.QRect(QtCore.QPoint(self.width() // 2, self.rect_right.top()),
                                         self.rect_right.bottomRight())
        self.rect_y_left = self.rect_x_left.adjusted(0, self.rect_x_left.height(),
                                                     0, self.rect_x_left.height())
        self.rect_y_right = self.rect_x_left.adjusted(0, self.rect_x_right.height(),
                                                      0, self.rect_x_right.height())
        self.rect_z_left = self.rect_x_left.adjusted(0, self.rect_x_left.height() * 2,
                                                     0, self.rect_x_left.height() * 2)
        self.rect_z_right = self.rect_x_left.adjusted(0, self.rect_x_right.height() * 2,
                                                      0, self.rect_x_right.height() * 2)

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

    def mousePressEvent(self, event):
        # type: (QtCore.QEvent) -> None
        event.accept()
        if event.type() != QtCore.QEvent.MouseButtonPress:
            return
        if self.rect_close.contains(event.pos()):
            if event.button() == QtCore.Qt.LeftButton:
                self.close()

    def mouseMoveEvent(self, event):
        # type: (QtCore.QEvent) -> None
        """ mouse movement """
        event.accept()
        if self.rect_close.contains(event.pos()):
            if not self._enter_close:
                self.color_close = self.color_in_close
                self._enter_close = True
                print("enter")
        else:
            self.color_close = self.color_out_close
            self._enter_close = False

        self.update()

    def leaveEvent(self, event):
        """ mouse exit the window """
        self.color_close = self.color_out_close
        self._enter_close = False

        self.update()

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

        painter.fillPath(path, self.brush_white)

        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceAtop)
        painter.drawPixmap(self.rect(),
                           self.px_background)

        # title
        painter.drawPixmap(self.rect_title,
                           self.px_title)

        # close
        self.img_close.fill(self.color_close)
        self.img_close.setAlphaChannel(self.px_close.toImage())
        painter.drawImage(self.rect_close,
                          self.img_close)
        # painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        # painter.drawPixmap(self.rect_close,
        #                    self.px_close)
        # painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceAtop)
        # painter.fillRect(self.rect_close,
        #                  self.brush_close)

        # left arrows
        painter.drawPixmap(self.rect_left,
                           self.px_left)
        painter.drawPixmap(self.rect_left.adjusted(0, self.rect_left.height(),
                                                   0, self.rect_left.height()),
                           self.px_left)
        painter.drawPixmap(self.rect_left.adjusted(0, self.rect_left.height() * 2,
                                                   0, self.rect_left.height() * 2),
                           self.px_left)

        # X
        painter.drawPixmap(self.rect_center,
                           self.px_x)
        # Y
        painter.drawPixmap(self.rect_center.adjusted(0, self.rect_center.height(),
                                                     0, self.rect_center.height()),
                           self.px_y)
        # Z
        painter.drawPixmap(self.rect_center.adjusted(0, self.rect_center.height() * 2,
                                                     0, self.rect_center.height() * 2),
                           self.px_z)

        # right arrows
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
