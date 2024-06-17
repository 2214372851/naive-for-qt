from PySide6 import QtCore, QtGui, QtWidgets
from ..NCore.Core import Size, Switch


class Avatar(QtWidgets.QLabel):
    def __init__(self,
                 icon: str | QtGui.QImage,
                 tip: str = None,
                 size: Size | int = Size.medium,
                 circle: Switch = Switch.off,
                 background: tuple[int, int, int, int] = (0, 0, 0, 0)):
        super().__init__()
        self.setObjectName('main-avatar')
        self.setProperty('Circle', circle.value)
        # noinspection PyArgumentList
        self.setStyleSheet('background-color: rgba({}, {}, {}, {});'.format(*QtGui.QColor(*background).getRgb()))
        if tip: self.setToolTip(tip)
        self._size = size
        self.setupUi(icon)

    def setupUi(self, icon: str | QtGui.QImage):
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        if isinstance(self._size, int):
            self.setFixedSize(self._size, self._size)
        else:
            self.setProperty('Size', self._size.value)
            self.setFixedSize(*{
                Size.small: (28, 28),
                Size.large: (40, 40),
                Size.medium: (34, 34),
            }.get(self._size, (34, 34)))
        if isinstance(icon, str):
            self.setText(icon)
        else:
            self.setPixmap(QtGui.QPixmap.fromImage(icon.scaled(self.size() * .7)))
