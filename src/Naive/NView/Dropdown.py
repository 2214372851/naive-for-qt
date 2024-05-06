from PySide6 import QtCore, QtWidgets, QtGui
from .Button import Button


class Menu(QtWidgets.QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(
            self.windowFlags() |
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.NoDropShadowWindowHint
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground)
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 0)
        shadow.setColor(QtGui.QColor('#444'))
        shadow.setBlurRadius(10)
        self.setGraphicsEffect(shadow)


class Dropdown(Button):

    def setupUi(self):
        self.setProperty('name', 'main-dropdown-menu')
        list_menu = []
        self.menu = Menu(self)
        list_menu.append(self.menu)
        m1 = QtWidgets.QMenu(self.menu)
        list_menu.append(m1)
        m1.setTitle('子菜单')
        m1.addAction(QtGui.QAction('你好', self))
        m1.addAction(QtGui.QAction('你好2', self))
        m1.addAction(QtGui.QAction('你好3', self))
        m2 = QtWidgets.QMenu(self.menu)
        list_menu.append(m2)
        m2.setTitle('子菜单2')
        m2.addAction(QtGui.QAction('你好', self))
        m2.addAction(QtGui.QAction('你好2', self))
        m2.addAction(QtGui.QAction('你好3', self))
        self.menu.addMenu(m1)
        self.menu.addMenu(m2)
        self.menu.addAction(QtGui.QAction('特殊他', self))
        self.setMenu(self.menu)
        # for menu in list_menu:
