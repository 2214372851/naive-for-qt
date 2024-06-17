from PySide6 import QtCore, QtGui, QtWidgets
from ..NView.Base import BashVBoxLayout, BashHBoxLayout
from ..NCore.Core import Size, Switch


class Card(QtWidgets.QFrame):
    def __init__(self,
                 title: str,
                 content: QtWidgets.QWidget,
                 extra: QtWidgets.QWidget = None,
                 footer: QtWidgets.QWidget = None,
                 action: QtWidgets.QWidget = None,
                 size: Size = Size.medium,
                 bordered: Switch = Switch.on,
                 hover: Switch = Switch.off):
        super().__init__()
        self.setObjectName('main-card')
        self.setProperty('Size', size.value)
        self.setProperty('Bordered', bordered.value)
        self._title: QtWidgets.QLabel | None = None
        self._extra: QtWidgets.QWidget | None = None
        self._header: QtWidgets.QWidget | None = None
        if hover == Switch.on:
            self.enterEvent = self._addShadow
            self.leaveEvent = self._clearShadow
        self.setupUi(title, content, extra, footer, action)

    def setupUi(self,
                title: str,
                content: QtWidgets.QWidget,
                extra: QtWidgets.QWidget = None,
                footer: QtWidgets.QWidget = None,
                action: QtWidgets.QWidget = None, ):
        self.setLayout(BashVBoxLayout())
        self.layout().setSpacing(10)

        self._header = QtWidgets.QWidget()
        self._header.setObjectName('main-card-header')
        self._header.setLayout(BashHBoxLayout())

        self._addTitle(title)
        self._addExtra(extra)
        self.layout().addWidget(self._header)
        self._addContent(content)
        self._addFooter(footer)
        self._addAction(action)
        self.setMinimumSize(self.sizeHint())

    def _addTitle(self, title: str):
        self._title = QtWidgets.QLabel()
        self._title.setObjectName('main-card-title')
        self._title.setText(title)
        self._header.setFixedHeight(self._title.sizeHint().height()+2)
        self._header.layout().addWidget(self._title)
        self._header.layout().addStretch(1)

    def _addExtra(self, extra: QtWidgets.QWidget):
        if not extra: return
        extra.setObjectName('main-card-extra')
        self._header.setFixedHeight(max(self._title.sizeHint().height(), extra.sizeHint().height()))
        self._header.layout().addWidget(extra)

    def _addContent(self, content: QtWidgets.QWidget):
        content.setObjectName('main-card-content')
        content.setMinimumHeight(content.sizeHint().height())
        self.layout().addWidget(content)

    def _addFooter(self, footer: QtWidgets.QWidget):
        if not footer: return
        footer.setObjectName('main-card-footer')
        footer.setFixedHeight(footer.sizeHint().height())
        self.layout().addWidget(footer)

    def _addAction(self, action: QtWidgets.QWidget):
        if not action: return
        action.setObjectName('main-card-action')
        action.setFixedHeight(action.sizeHint().height())
        self.layout().addWidget(action)

    def _addShadow(self, event):
        print(event)
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QtGui.QColor(0, 0, 0, 50))
        self.setGraphicsEffect(shadow)
        super().enterEvent(event)

    def _clearShadow(self, event):
        # noinspection PyTypeChecker
        self.setGraphicsEffect(None)
        self.update()
        super().leaveEvent(event)
