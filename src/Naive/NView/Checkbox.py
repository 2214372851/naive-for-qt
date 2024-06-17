from PySide6 import QtCore, QtWidgets, QtGui
from ..NCore.Core import ButtonType, Switch, Size


class Checkbox(QtWidgets.QCheckBox):
    def __init__(self, text: str, size: Size = Size.large, parent=None):
        super().__init__(text, parent)
        self.setObjectName('main-checkbox')
        self.setProperty('Size', size.value)
