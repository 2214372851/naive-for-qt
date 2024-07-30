import time
import typing
from pathlib import Path

import requests
from PySide6 import QtWidgets, QtGui, QtCore
from requests_toolbelt.multipart import encoder

from . import BashVBoxLayout
from . import ProgressBar
from ..NCore.Core import OpenType, StateStyle
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


class ApiUpload(QtWidgets.QFrame):
    schedule = QtCore.Signal(encoder.MultipartEncoderMonitor)

    def __init__(self, api: str, params: dict = None, cookies: dict = None, callBack: typing.Callable = None):
        super().__init__()
        self.api = api
        self.params = params if params else {}
        self.__cookies = cookies if cookies else {}
        self.__upload_progress = ProgressBar()
        self.__upload = Upload(openType=OpenType.file, callBack=self.initUpload)
        self.__callBack = callBack
        self.__start_time = 0
        self.setupUi()

    def setupUi(self):
        self.__upload_progress.setFixedHeight(30)
        self.schedule.connect(self.setValue)
        self.setLayout(QtWidgets.QVBoxLayout())

        self.layout().addWidget(self.__upload)
        self.layout().addWidget(self.__upload_progress)

    @threadFunc()
    def uploading(self, path: Path):
        try:
            e = encoder.MultipartEncoder(
                fields={'file': (path.name, path.open('rb'), 'application/x-zip-compressed'),
                        **self.params}
            )
            m = encoder.MultipartEncoderMonitor(e, self.schedule.emit)
            header = {"Content-Type": m.content_type}
            result = requests.post(url=self.api, data=m, headers=header, cookies=self.__cookies)
            if self.__callBack:
                self.__callBack(result)
        except requests.exceptions.HTTPError as http_err:
            self.__upload_progress.setState(StateStyle.error)
        except requests.exceptions.RequestException as req_err:
            self.__upload_progress.setState(StateStyle.error)
        finally:
            self.__upload.setEnabled(True)

    def initUpload(self, path: Path):
        self.__upload_progress.reset()
        self.__upload_progress.setState(StateStyle.default)
        self.__upload.setEnabled(True)
        self.__start_time = time.time()
        self.uploading(path)

    def setValue(self, e: encoder.MultipartEncoderMonitor):
        self.__upload_progress.setValue(e.bytes_read)
        value = e.bytes_read
        self.__upload_progress.setValue(value)
        if value == e.len:
            self.__upload_progress.setState(StateStyle.success)
