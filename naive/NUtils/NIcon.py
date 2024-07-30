from pathlib import Path
from PySide6.QtCore import QDir


def init_icon():
    ICON_PATH = Path(__file__).parent.parent / 'static' / 'lightIcon'
    QDir.addSearchPath('Icons', ICON_PATH)

