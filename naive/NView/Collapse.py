from PySide6 import QtCore, QtGui, QtWidgets
from typing import TypedDict, List, Callable, Union


class CollapseWidgetItem(TypedDict):
    widget: QtWidgets.QWidget


class CollapseItem(TypedDict):
    title: str
    icon: str
    callback: Union[Callable, None]
    child: List[Union['CollapseItem', CollapseWidgetItem]]


class Collapse(QtWidgets.QTreeWidget):
    def __init__(self, data: list[CollapseWidgetItem | CollapseItem]):
        super().__init__()
        self.setObjectName("main-collapse")
        self.data = data
        self.setupUi()

    def setupUi(self):
        self.setHeaderHidden(True)
        self._generateTree(self, self.data)
        self.itemClicked.connect(self.onItemClicked)

    def _generateTree(self, parent, child):
        for item_data in child:
            item = QtWidgets.QTreeWidgetItem(parent)

            title = item_data.get('title')
            widget = item_data.get('widget')
            icon = item_data.get('icon')
            callback = item_data.get('callback')
            child = item_data.get('child')

            if widget:
                self.setItemWidget(item, 0, widget)
                return
            if title:
                item.setText(0, title)
            if icon:
                item.setIcon(0, QtGui.QIcon(icon))
            item.setData(0, QtCore.Qt.ItemDataRole.UserRole, callback)
            self._generateTree(item, child)

    @staticmethod
    def onItemClicked(item: QtWidgets.QTreeWidgetItem):
        if callable(call := item.data(0, QtCore.Qt.ItemDataRole.UserRole)):
            call()
