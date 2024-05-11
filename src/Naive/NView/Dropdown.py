from PySide6 import QtCore, QtWidgets, QtGui
from .Button import Button
from typing import TypedDict, Callable, Union, List
from src.Naive.NView.Base import BashMenu


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
        root_menu = BashMenu(self)
        self.addNode(root_menu, self._menus)
        self.setMenu(root_menu)

    def addNode(self, parent, data):
        for item in data:
            name = item.get('name', '')
            icon = item.get('icon', '')
            callback = item.get('callback', None)
            children = item.get('children', [])
            if children:
                node = BashMenu(parent)
                node.setTitle(name)
                parent.addMenu(node)
                self.addNode(node, children)
            else:
                node = QtGui.QAction(name, self)
                callback and node.triggered.connect(callback)
                parent.addAction(node)
            icon and node.setIcon(QtGui.QIcon(icon))
