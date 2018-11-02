import sys
from PySide2 import QtWidgets, QtCore, QtGui
import interface

if __name__ == '__main__':
    qt_app = QtWidgets.QApplication()

    interface.load()

    sys.exit(qt_app.exec_())
