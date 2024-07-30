import sys
from pathlib import Path

from PySide6 import QtWidgets, QtCore, QtGui
import win32mica


class BashWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(BashVBoxLayout())
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

    def show(self):
        super().show()
        self.setStyleSheet(Path(__file__).parent.parent.joinpath("static", "light.css").read_text("utf-8"))


class BashMainWindow(BashWindow):
    """Borderless window base class"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(
            QtCore.Qt.WindowType.Window |
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowSystemMenuHint |
            QtCore.Qt.WindowType.WindowMinimizeButtonHint |
            QtCore.Qt.WindowType.WindowMaximizeButtonHint
        )
        self.setMouseTracking(True)

        self.base_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.base_shadow.setBlurRadius(15)
        self.base_shadow.setOffset(0, 0)
        self.base_shadow.setColor(QtGui.QColor(0, 0, 0, 150))
        self.setGraphicsEffect(self.base_shadow)
        self._direction = None
        self.bottom_edge = None
        self.top_edge = None
        self.right_edge = None
        self.left_edge = None
        self.layout().setContentsMargins(5, 5, 5, 5)

    def mouseMoveEvent(self, event):
        self.left_edge = QtCore.QRect(0, 0, 10, self.height())
        self.right_edge = QtCore.QRect(self.width() - 10, 0, self.width(), self.height())
        self.top_edge = QtCore.QRect(0, 0, self.width(), 10)
        self.bottom_edge = QtCore.QRect(0, self.height() - 10, self.width(), self.height())
        if self.isMaximized(): return
        mouse_pos = event.position().toPoint()
        self._mouseCursor(
            self.left_edge.contains(mouse_pos),
            self.right_edge.contains(mouse_pos),
            self.top_edge.contains(mouse_pos),
            self.bottom_edge.contains(mouse_pos)
        )
        return super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        self._mouseResizeWindow(event)
        return super().mousePressEvent(event)

    def _mouseCursor(self, left_edge, right_edge, top_edge, bottom_edge):
        left_top_edge = (left_edge, top_edge)
        left_bottom_edge = (left_edge, bottom_edge)
        right_top_edge = (right_edge, top_edge)
        right_bottom_edge = (right_edge, bottom_edge)
        if not any((left_edge, right_edge, top_edge, bottom_edge)):
            self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
            self._direction = None
            return
        if all(left_top_edge):
            self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
            self._direction = QtCore.Qt.Edge.LeftEdge | QtCore.Qt.Edge.TopEdge
        elif all(right_bottom_edge):
            self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
            self._direction = QtCore.Qt.Edge.RightEdge | QtCore.Qt.Edge.BottomEdge
        elif all(left_bottom_edge):
            self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
            self._direction = QtCore.Qt.Edge.LeftEdge | QtCore.Qt.Edge.BottomEdge
        elif all(right_top_edge):
            self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
            self._direction = QtCore.Qt.Edge.RightEdge | QtCore.Qt.Edge.TopEdge
        elif left_edge:
            self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
            self._direction = QtCore.Qt.Edge.LeftEdge
        elif right_edge:
            self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
            self._direction = QtCore.Qt.Edge.RightEdge
        elif top_edge:
            self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
            self._direction = QtCore.Qt.Edge.TopEdge
        elif bottom_edge:
            self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
            self._direction = QtCore.Qt.Edge.BottomEdge

    def _mouseResizeWindow(self, event):
        if event.button() != QtCore.Qt.MouseButton.LeftButton: return
        if self._direction is None: return
        self.windowHandle().startSystemResize(self._direction)

    def enterEvent(self, event):
        self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
        self._direction = None
        return super().enterEvent(event)

    def showMaximized(self):
        self.layout().setContentsMargins(0, 0, 0, 0)
        super().showMaximized()

    def showNormal(self):
        self.layout().setContentsMargins(5, 5, 5, 5)
        super().showNormal()


class BashMicaWindow(BashWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._mica()

    def _mica(self):
        win32mica.ApplyMica(HWND=self.winId(), Theme=win32mica.MicaTheme.AUTO, Style=win32mica.MicaStyle.DEFAULT)


class BashHBoxLayout(QtWidgets.QHBoxLayout):
    """Horizontal layout without base style"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)


class BashVBoxLayout(QtWidgets.QVBoxLayout):
    """Vertical layout without base style"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)


class BashMenu(QtWidgets.QMenu):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('main-menu')
        self.setWindowFlags(
            self.windowFlags() |
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.NoDropShadowWindowHint
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
