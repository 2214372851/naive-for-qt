from PySide6 import QtWidgets


class Input(QtWidgets.QLineEdit):
    def __init__(self, placeholder: str = None):
        super().__init__()
        self.setObjectName('main-input')
        self.setPlaceholderText(placeholder)

    def contextMenuEvent(self, e):
        pass


class Textarea(QtWidgets.QTextEdit):
    def __init__(self, placeholder: str = None):
        super().__init__()
        self.setObjectName('main-input')
        self.setPlaceholderText(placeholder)

    def contextMenuEvent(self, e):
        pass


class InputNumber(QtWidgets.QSpinBox):
    def __init__(self, max: int = 100, min: int = 0):
        super().__init__()
        self.setMaximum(max)
        self.setMinimum(min)
        self.setObjectName('main-input')
