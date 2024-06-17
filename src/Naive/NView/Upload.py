import typing
from pathlib import Path

from PySide6 import QtWidgets, QtGui, QtCore
from ..NView.Base import BashVBoxLayout, BashHBoxLayout
from ..NCore.Core import OpenType
from ..NUtils.NFunc import threadFunc


class Upload(QtWidgets.QFrame):
    def __init__(self, openType=OpenType.file, callBack: typing.Callable = None):
        super().__init__()
        self.setObjectName("main-upload")
        self._open_type = openType
        self._callable = callBack
        self.setupUi()

    def setupUi(self):
        self.setLayout(BashVBoxLayout())
        self.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title = QtWidgets.QLabel('点击或者拖动文件到该区域来上传')
        title.setObjectName('title')
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout().addWidget(title)
        content = QtWidgets.QLabel('请不要上传敏感数据，比如你的银行卡号和密码，信用卡号有效期和安全码')
        content.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        content.setWordWrap(True)
        self.layout().addWidget(content)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        """
        Drag event
        :param event:
        :return:
        """
        event.accept()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        """
        Drag event
        :param event:
        :return:
        """
        drag_filename = Path(event.mimeData().text().replace('file:///', ''))
        if not self._callable: return
        if self._open_type == OpenType.folder and drag_filename.is_dir():
            self._callable(drag_filename)
        elif self._open_type == OpenType.file and drag_filename.is_file():
            self._callable(drag_filename)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            if self._open_type == OpenType.file:
                path, _ = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件')
            elif self._open_type == OpenType.folder:
                path = QtWidgets.QFileDialog.getExistingDirectory(self, '打开文件夹')
            else:
                raise TypeError('File type error')
            if not self._callable or not path: return
            path = Path(path)
            if self._open_type == OpenType.folder and path.is_dir():
                self._callable(path)
            elif self._open_type == OpenType.file and path.is_file():
                self._callable(path)


class ApiUpload(Upload):
    def __init__(self, openType=OpenType.file):
        super().__init__(openType=openType)
        # TODO: 由于进度条未实现暂且延后开发该组件

    def uploading(self, path: Path):
        pass
