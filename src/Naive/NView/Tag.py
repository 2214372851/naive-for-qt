from PySide6 import QtCore, QtWidgets, QtGui
from src.Naive.NCore.Core import TagType, Size, Switch


class Tag(QtWidgets.QLabel):
    def __init__(self,
                 text: str,
                 size: Size = Size.small,
                 round: Switch = Switch.on,
                 style_type: TagType = TagType.default,
                 parent=None):
        super().__init__(text, parent)
        print(size)
        self.setObjectName('main-tag')
        self.setProperty('type', style_type.value)
        self.setProperty('Size', size.value)
        self.setProperty('Round', round.value)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def resizeEvent(self, event):
        self.setFixedSize(self.sizeHint())
        super().resizeEvent(event)
