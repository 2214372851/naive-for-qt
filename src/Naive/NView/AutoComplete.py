from functools import partial

from PySide6 import QtWidgets, QtCore, QtGui
from ..NView.Base import BashMenu


class AutoComplete(QtWidgets.QLineEdit):
    def __init__(self, completion: list):
        super().__init__()
        self.setObjectName('main-auto-complete')
        self.setupUi()
        self._actions = []
        self._completion_result = completion
        self._menu = BashMenu(self)

    def setupUi(self):
        self.setPlaceholderText('请输入内容')

    def textCompletion(self):
        if self._actions:
            for action in self._actions:
                self._menu.removeAction(action)
        self._menu.popup(self.mapToGlobal(self.rect().bottomLeft()))
        result = filter(lambda item: item.startswith(self.text()), self._completion_result)
        for completion in result:
            action = QtGui.QAction(completion, self._menu)
            action.triggered.connect(partial(self.setText, completion))
            self._menu.addAction(action)
            self._actions.append(action)
        self.setFocus()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Control:
            self.textCompletion()
            event.ignore()
        super().keyPressEvent(event)
