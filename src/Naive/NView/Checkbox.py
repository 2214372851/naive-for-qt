from PySide6 import QtCore, QtWidgets, QtGui


class Checkbox(QtWidgets.QCheckBox):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setObjectName('main-checkbox')
