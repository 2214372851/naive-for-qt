from PySide6 import QtWidgets, QtCore, QtGui


class Radio(QtWidgets.QRadioButton):
    def __init__(self, text: str):
        super().__init__()
        self.setObjectName('main-radio')
        self.setText(text)
