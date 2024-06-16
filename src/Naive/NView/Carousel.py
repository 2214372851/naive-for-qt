from PySide6 import QtCore, QtGui, QtWidgets
from Naive.NView.Base import BashVBoxLayout, BashHBoxLayout
from Naive.NCore.Core import Switch
from functools import partial
from typing import Callable, TypedDict, List


class CarouselItem(TypedDict):
    src: str
    callback: Callable[[int], None]


class Carousel(QtWidgets.QFrame):
    def __init__(self,
                 data: List[CarouselItem],
                 dots: Switch = Switch.on,
                 wheel: Switch = Switch.off,
                 arrow: Switch = Switch.off,
                 autoplay: Switch = Switch.off):
        super(Carousel, self).__init__()
        self.setObjectName('main-carousel')
        self._canvas = QtWidgets.QWidget(self)
        self._dots_widget = QtWidgets.QWidget(self)
        self._next_button = None
        self._previous_button = None
        self._animation = QtCore.QPropertyAnimation(self._canvas, b'pos')
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.next)
        self._stack = []
        self._find_map = {}
        self._show_index = 1
        self._dots_flag = None
        self._dots = dots
        self._wheel = wheel
        self._arrow = arrow
        self._autoplay = autoplay
        self._data = data
        self.setupUi()

    def setupUi(self):
        images = self._data
        self._find_map = {
            0: len(images),
            len(images) + 1: 1,
        }
        self._dots_widget.setLayout(QtWidgets.QHBoxLayout())
        if self._dots == Switch.on:
            for index in range(len(images)):
                dots_index = index + 1
                dots_button = QtWidgets.QPushButton()
                dots_button.setObjectName(str(dots_index))
                dots_button.setFixedWidth(10)
                dots_button.setProperty('name', 'main-carousel-dots')
                dots_button.clicked.connect(partial(self.to, dots_index))
                self._dots_widget.layout().addWidget(dots_button)
        self._dots_widget.setFixedSize(self._dots_widget.sizeHint())

        images.insert(0, images[-1])
        images.append(images[1])
        self._canvas.setLayout(BashHBoxLayout())
        for index, image in enumerate(images):
            label = QtWidgets.QLabel()
            label.setPixmap(QtGui.QPixmap(image.get('src')))
            label.setScaledContents(True)
            label.setFixedSize(self.size())
            label.mouseReleaseEvent = partial(self._callBack, image.get('callback'))
            self._stack.append(label)
            self._canvas.layout().addWidget(label)
        if self._arrow == Switch.on:
            self._next_button = QtWidgets.QPushButton('>', parent=self)
            self._previous_button = QtWidgets.QPushButton('<', parent=self)
            self._next_button.setProperty('name', 'main-carousel-controls')
            self._previous_button.setProperty('name', 'main-carousel-controls')
            self._next_button.setFixedSize(30, 40)
            self._previous_button.setFixedSize(30, 40)
            self._next_button.clicked.connect(self.next)
            self._previous_button.clicked.connect(self.previous)
        if self._autoplay == Switch.on:
            self._timer.start(3000)

    def resizeEvent(self, event):
        for item in self._stack:
            item.setFixedSize(self.size())
        self._canvas.resize(self.size().width() * len(self._stack), self.size().height())
        self._canvas.move(-self.size().width() * self._show_index, 0)
        if self._dots == Switch.on:
            self._dots_widget.move(
                int((self.width() - self._dots_widget.width()) / 2),
                self.height() - self._dots_widget.height()
            )
        if self._arrow == Switch.on:
            self._next_button.move(
                self.width() - self._next_button.width(),
                int((self.height() - self._next_button.height()) / 2)
            )
            self._previous_button.move(
                0,
                int((self.height() - self._next_button.height()) / 2)
            )

        super().resizeEvent(event)

    def _toggle(self):
        # noinspection PyTypeChecker
        btn: QtWidgets.QPushButton = self._dots_widget.findChild(
            QtWidgets.QPushButton,
            str(self._find_map.get(self._show_index, self._show_index))
        )
        if self._dots_flag:
            self._dots_flag.setStyleSheet('background: rgba(255, 255, 255, .3);')
        if btn:
            btn.setStyleSheet('background: rgba(255, 255, 255, 1);')
            self._dots_flag = btn
        self._animation.setStartValue(self._canvas.pos())
        self._animation.setEndValue(QtCore.QPoint(-self.size().width() * self._show_index, 0))
        self._animation.setDuration(300)
        self._animation.start()

    def next(self):
        if self._animation.state() != self._animation.State.Stopped: return
        self._show_index += 1
        if self._show_index == len(self._stack):
            self._canvas.move(-self.width(), 0)
            self._show_index = 2
        self._toggle()

    def previous(self):
        if self._show_index == 0:
            self._canvas.move((self.width() * 2) - self._canvas.width(), 0)
            self._show_index = len(self._stack) - 2
        self._show_index -= 1
        self._toggle()

    def to(self, index):
        self._show_index = index
        self._toggle()

    def wheelEvent(self, event):
        super().wheelEvent(event)
        if self._wheel == Switch.off: return
        if event.angleDelta().y() > 0:
            self.previous()
        else:
            self.next()

    def enterEvent(self, event):
        super().enterEvent(event)
        if self._autoplay == Switch.off: return
        self._timer.stop()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        if self._autoplay == Switch.off: return
        self._timer.start()

    def _callBack(self, callBack: Callable, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            callBack()
