from PySide6 import QtCore, QtGui, QtWidgets


class Scroll(QtWidgets.QScrollArea):
    def __init__(self, widget: QtWidgets.QWidget, parent=None):
        super().__init__(parent)
        self.setObjectName('main-scroll')
        self.setWidgetResizable(True)
        self.setWidget(widget)
