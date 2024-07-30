from ..NCore.Core import Size
from PySide6 import QtCore, QtWidgets, QtGui


class Select(QtWidgets.QComboBox):
    def __init__(self, items: list[str] = None, size: Size = Size.medium):
        super().__init__()
        self.setObjectName('main-select')
        self.setProperty('Size', size.value)
        self._items = items
        self.setupUi()

    def setupUi(self):
        if self._items is not None:
            self.addItems(self._items)

    def setItems(self, items: list[str]):
        self._items = items
        self.clear()
        self.addItems(self._items)

    def text(self):
        return self.currentText()
