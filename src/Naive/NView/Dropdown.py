from PySide6 import QtCore, QtWidgets, QtGui
from .Button import Button
from typing import TypedDict, Callable, Union, List


class DropdownMenu(QtWidgets.QMenu):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(
            self.windowFlags() |
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.NoDropShadowWindowHint
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)


class DropdownItem(TypedDict):
    name: str
    callback: Union[Callable, None]
    icon: str | None
    children: List['DropdownItem'] | None


class Dropdown(Button):
    def __init__(self, menus: List[DropdownItem], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._menus = menus
        self.setupUi()

    def setupUi(self):
        self.setProperty('name', 'main-dropdown-menu')
        root_menu = DropdownMenu(self)
        self.addNode(root_menu, self._menus)
        self.setMenu(root_menu)

    def addNode(self, parent, data):
        for item in data:
            name = item.get('name', '')
            callback = item.get('callback', None)
            children = item.get('children', [])
            if children:
                node = DropdownMenu(parent)
                node.setTitle(name)
                parent.addMenu(node)
                self.addNode(node, children)
            else:
                node = QtGui.QAction(name, self)
                if callback:
                    node.triggered.connect(callback)
                parent.addAction(node)
