from PySide6 import QtCore, QtWidgets, QtGui
from ..NCore.Core import TextType, Switch


class H1(QtWidgets.QLabel):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setObjectName('main-h1')


class H2(QtWidgets.QLabel):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setObjectName('main-h2')


class H3(QtWidgets.QLabel):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setObjectName('main-h3')


class H4(QtWidgets.QLabel):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setObjectName('main-h4')


class Text(QtWidgets.QLabel):
    def __init__(self,
                 text: str,
                 style_type: TextType = TextType.default,
                 strong: Switch = Switch.off,
                 underline: Switch = Switch.off,
                 code: Switch = Switch.off,
                 delete: Switch = Switch.off,
                 parent=None):
        super().__init__(text, parent)
        self.setObjectName('main-text')
        self.setProperty('type', style_type.value)
        self.setProperty('Strong', strong.value)
        self.setProperty('Underline', underline.value)
        self.setProperty('Code', code.value)
        self.setProperty('Delete', delete.value)
