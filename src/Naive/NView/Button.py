from typing import Callable

from PySide6 import QtCore, QtWidgets

from src.Naive.NCore.Core import ButtonType, Switch, Size


class Button(QtWidgets.QPushButton):
    def __init__(self,
                 text: str = None,
                 callback: Callable = None,
                 size: Size = Size.medium,
                 strong: Switch = Switch.off,
                 round: Switch = Switch.off,
                 style_type: ButtonType = ButtonType.default):
        super().__init__(text)
        self.setObjectName('main-button')
        self.setProperty('type', style_type.value)
        self.setProperty('Strong', strong.value)
        self.setProperty('Round', round.value)
        self.setProperty('Size', size.value)
        self.setCallBack(callback)
        self.setupUi()

    def setupUi(self):
        pass

    def enterEvent(self, event):
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
        super().leaveEvent(event)

    def setCallBack(self, callback: Callable):
        if not callback: return
        self.clicked.connect(callback)
