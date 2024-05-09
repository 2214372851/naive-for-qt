from PySide6 import QtCore, QtWidgets, QtGui


class Tag(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('main-tag')
        self.setupUi()

    def setupUi(self):
        self.show()
        # self.setFixedSize(self.sizeHint())
