from PySide6 import QtWidgets, QtGui, QtCore
from typing import Tuple
from ..NCore.Core import StateStyle


class ProgressBar(QtWidgets.QProgressBar):
    def __init__(self, limits: Tuple[int, int] = (0, 100)):
        super().__init__()
        self.setObjectName('main-progress-bar')
        self.setRange(*limits)
        self.setState(StateStyle.default)
        self.setValue(66)

    def setState(self, state: StateStyle):
        self.setProperty('state', state.value)
        self.style().polish(self)
        self.update()
