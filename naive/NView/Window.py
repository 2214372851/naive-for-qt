import os
from functools import partial
from typing import Callable, TypedDict, Union
import win32mica

from PySide6 import QtCore, QtGui, QtWidgets

from naive.NUtils.NIcon import init_icon
from naive.NView.Base import BashVBoxLayout, BashHBoxLayout, BashMainWindow, BashMicaWindow


class MainTitleBar(QtWidgets.QWidget):
    def __init__(self, title: str, version: str, icon: str, parent=None):
        super().__init__(parent)
        self.setObjectName('main-title-bar')
        self.right_widget = None
        self.left_widget = None
        self.icon = None
        self.title = None
        self.version = None
        self.min_button = None
        self.max_button = None
        self.close_button = None
        self.setupUi(title, version, icon)

    def setupUi(self, title: str, version: str, icon: str):
        self.setFixedHeight(34)
        self.setLayout(BashHBoxLayout())
        self.right_widget = QtWidgets.QWidget()
        self.left_widget = QtWidgets.QWidget()

        self.icon = QtWidgets.QLabel()
        self.icon.setObjectName('main-icon')
        self.icon.mouseDoubleClickEvent = lambda x: os.system('start https://www.naiveui.com')
        self.title = QtWidgets.QLabel()
        self.title.setObjectName('main-title')
        self.version = QtWidgets.QLabel()
        self.version.setObjectName('main-version')
        self.min_button = QtWidgets.QPushButton()
        self.min_button.setObjectName('min-button')
        self.max_button = QtWidgets.QPushButton()
        self.max_button.setObjectName('max-button')
        self.close_button = QtWidgets.QPushButton()
        self.close_button.setObjectName('close-button')

        # init widget layout
        self.layout()
        self.right_widget.setLayout(BashHBoxLayout())
        self.left_widget.setLayout(BashHBoxLayout())
        self.right_widget.layout().setDirection(QtWidgets.QHBoxLayout.Direction.RightToLeft)
        self.right_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.left_widget.layout().setDirection(QtWidgets.QHBoxLayout.Direction.LeftToRight)
        self.left_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.left_widget.layout().setContentsMargins(7, 0, 0, 0)
        self.left_widget.layout().setSpacing(12)

        # init button icon
        self.icon.setPixmap(QtGui.QPixmap(icon))
        self.title.setText(title)
        self.version.setText(version)
        self.max_button.setIcon(QtGui.QIcon('Icons:square.svg'))
        self.close_button.setIcon(QtGui.QIcon('Icons:close.svg'))
        self.close_button.setToolTip('关闭')
        self.min_button.setIcon(QtGui.QIcon('Icons:minus.svg'))
        self.min_button.setToolTip('关闭')

        # init button pos
        self.left_widget.layout().addWidget(self.icon)
        self.left_widget.layout().addWidget(self.title)
        self.left_widget.layout().addWidget(self.version)
        self.right_widget.layout().addWidget(self.close_button)
        self.right_widget.layout().addWidget(self.max_button)
        self.right_widget.layout().addWidget(self.min_button)
        self.icon.setScaledContents(True)
        self.icon.setFixedSize(20, 20)
        self.close_button.setFixedSize(34, 34)
        self.close_button.clicked.connect(self.__close_window)
        self.min_button.setFixedSize(34, 34)
        self.min_button.clicked.connect(self.__min_window)
        self.max_button.setFixedSize(34, 34)
        self.max_button.clicked.connect(self.__toggleMaxState)

        self.layout().addWidget(self.left_widget)
        self.layout().addWidget(self.right_widget)

    def mouseMoveEvent(self, event):
        self.window().windowHandle().startSystemMove()

    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.__toggleMaxState()

    def __toggleMaxState(self):
        if self.window().isMaximized():
            self.window().setStyleSheet('#main-window{border-radius:10px;}#close-button{border-top-right-radius:10px}')
            self.setToolTip('最大化')
            self.max_button.setIcon(QtGui.QIcon('Icons:square.svg'))
            self.window().showNormal()
        else:
            self.window().setStyleSheet('#main-window{border-radius:0;}#close-button{border-top-right-radius:0}')
            self.setToolTip('正常')
            self.max_button.setIcon(QtGui.QIcon('Icons:copy.svg'))
            self.window().showMaximized()

    def __close_window(self):
        self.window().close()

    def __min_window(self):
        self.window().showMinimized()


class MainSideBar(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('main-sidebar')
        self.lastItem: QtWidgets.QPushButton | None = None
        self.more_widget = QtWidgets.QFrame()
        self.add_callback = self._addMenu
        self._row_count = 0
        self._column_count = 0
        self._menu_count = 0
        self.setupUi()

    def setupUi(self):
        self.setFixedWidth(52)
        self.more_widget.setObjectName('main-more-widget')
        self.setLayout(BashVBoxLayout())
        self.layout().setContentsMargins(5, 15, 5, 0)
        self.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.more_widget.setLayout(QtWidgets.QGridLayout())
        self.more_widget.setWindowFlags(
            QtCore.Qt.WindowType.Window |
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowSystemMenuHint |
            QtCore.Qt.WindowType.WindowMinimizeButtonHint |
            QtCore.Qt.WindowType.WindowMaximizeButtonHint
        )

    def _more_show(self, event):
        self.more_widget.show()
        self.more_widget.move(
            event.globalPosition().toPoint() - QtCore.QPoint(-20, self._row_count * 52)
        )

    def _more_hide(self, event):
        self.more_widget.hide()

    def add(self, title: str, icon: str, callBack: Callable = None):
        self.add_callback(title, icon, callBack)

    def _more(self):
        item = QtWidgets.QPushButton(self)
        item.setToolTip('更多')
        item.enterEvent = self._more_show
        item.leaveEvent = self._more_hide
        item.setObjectName('menu-item')
        item.setIcon(QtGui.QIcon(QtGui.QIcon('Icons:more.svg')))
        item.setIconSize(QtCore.QSize(20, 20))
        item.setFixedSize(42, 42)
        self.layout().addWidget(item)

    def _addMoreMenu(self, title: str, icon: str, callBack: Callable = None):
        item = QtWidgets.QPushButton(self)
        item.setToolTip(title)
        item.clicked.connect(partial(self.__toggleItem, item, callBack))
        item.setObjectName('menu-item')
        item.setIcon(QtGui.QIcon(icon))
        item.setIconSize(QtCore.QSize(20, 20))
        item.setFixedSize(42, 42)
        # noinspection PyArgumentList
        self.more_widget.layout().addWidget(item, self._row_count, self._column_count)
        self._column_count += 1
        if self._column_count >= 3:
            self._row_count += 1
            self._column_count = 0

    def _addMenu(self, title: str, icon: str, callBack: Callable = None):
        item = QtWidgets.QPushButton(self)
        item.setToolTip(title)
        item.clicked.connect(partial(self.__toggleItem, item, callBack))
        item.setObjectName('menu-item')
        item.setIcon(QtGui.QIcon(icon))
        item.setIconSize(QtCore.QSize(20, 20))
        item.setFixedSize(42, 42)
        self.layout().addWidget(item)
        self._menu_count += 1
        if (self.window().height() - 34 - self._menu_count * (42 + 15)) < 50:
            self._more()
            self.add_callback = self._addMoreMenu

    def __toggleItem(self, item: QtWidgets.QPushButton, callBack: Callable):
        if self.lastItem:
            self.lastItem.setProperty('type', '')
            self.lastItem.style().polish(self.lastItem)
        item.setProperty('type', 'select')
        item.style().polish(item)
        self.lastItem = item
        if callBack:
            callBack()


class MainContent(QtWidgets.QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def addWidget(self, widget: QtWidgets.QWidget):
        widget.setObjectName('main-content-page')
        super().addWidget(widget)

    def to(self, index: int):
        self.setCurrentIndex(index)


class MenuItem(TypedDict):
    title: str
    icon: str
    page: Union[QtWidgets.QWidget, QtWidgets.QFrame, None]
    callback: Union[None, Callable]


class MainWindow(BashMainWindow):
    # 初始化图标库
    init_icon()

    def __init__(self, title: str, version: str, icon: str, menus: list[MenuItem] = None, parent=None):
        super().__init__(parent)
        self.content: MainContent | None = None
        self.side_bar: MainSideBar | None = None
        self.setupUi(title, version, icon)
        self.setupMenus(menus)

    def setupMenus(self, menus: list[MenuItem] = None):
        if not menus: return
        for index, menu in enumerate(menus):
            self.side_bar.add(
                menu.get('title'),
                menu.get('icon'),
                menu.get('callback') if menu.get('callback') else partial(self.content.to, index)
            )
            menu.get('page') and self.content.addWidget(menu.get('page'))

    def setupUi(self, title: str, version: str, icon: str):
        self.resize(800, 500)
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.setWindowIconText(title)
        main = QtWidgets.QFrame(self)
        main.setObjectName('main-window')
        main.setLayout(BashVBoxLayout())
        title_bar = MainTitleBar(title, version, icon)
        title_bar.enterEvent = super().enterEvent
        body = QtWidgets.QWidget()
        body.setObjectName('main-body')
        body.enterEvent = super().enterEvent
        body.setLayout(BashHBoxLayout())

        self.side_bar = MainSideBar(self)
        self.side_bar.enterEvent = super().enterEvent
        body.layout().addWidget(self.side_bar)

        self.content = MainContent()
        self.content.enterEvent = super().enterEvent
        body.layout().addWidget(self.content)

        main.layout().addWidget(title_bar)
        main.layout().addWidget(body)
        self.layout().addWidget(main)


class MicaWindow(BashMicaWindow):
    # 初始化图标库
    init_icon()

    def __init__(self, title: str, version: str, icon: str, menus: list[MenuItem] = None, parent=None):
        super().__init__(parent)
        self.content: MainContent | None = None
        self.side_bar: MainSideBar | None = None
        self.setupUi(title, version, icon)
        self.setupMenus(menus)

    def setupMenus(self, menus: list[MenuItem] = None):
        if not menus: return
        for index, menu in enumerate(menus):
            self.side_bar.add(
                menu.get('title'),
                menu.get('icon'),
                menu.get('callback') if menu.get('callback') else partial(self.content.to, index)
            )
            menu.get('page') and self.content.addWidget(menu.get('page'))

    def setupUi(self, title: str, version: str, icon: str):
        self.resize(800, 500)
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.setWindowIconText(title)
        main = QtWidgets.QFrame(self)
        main.setObjectName('main-mica-window')
        main.setLayout(BashVBoxLayout())
        body = QtWidgets.QWidget()
        body.setObjectName('main-mica-body')
        body.enterEvent = super().enterEvent
        body.setLayout(BashHBoxLayout())

        self.side_bar = MainSideBar(self)
        self.side_bar.enterEvent = super().enterEvent
        body.layout().addWidget(self.side_bar)

        self.content = MainContent()
        self.content.enterEvent = super().enterEvent
        body.layout().addWidget(self.content)

        main.layout().addWidget(body)
        self.layout().addWidget(main)

