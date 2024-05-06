from PySide6 import QtCore, QtWidgets, QtGui
from src.Naive.NCore.Core import Switch


class Divider(QtWidgets.QFrame):
    def __init__(self, vertical: Switch = Switch.off):
        super().__init__()
        self.setObjectName('main-divider')
        self._vertical = vertical
        self.setupUi()

    def setupUi(self):
        if self._vertical == Switch.on:
            self.setFixedWidth(1)
        else:
            self.setFixedHeight(1)
