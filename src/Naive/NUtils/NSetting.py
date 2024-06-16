from pathlib import Path

from PySide6.QtCore import QSettings

from Naive.NUtils import NIcon
from Naive.NCore import NMetaClass
from Naive.NCore import NTheme


class NSetting(metaclass=NMetaClass):
    """
    Apply global settings
    """

    theme: NTheme = NTheme.light

    def __init__(self, config_path: Path | str = None) -> None:
        """
        Args:
            config_path (Path | str): Path to the config file
        """
        self._config_data = None
        NIcon.initIconPath()
        self.load(config_path=config_path)

    def load(self, config_path: Path | str):
        """
        Load settings from config file
        Args:
            config_path (Path | str): Path of config file
        """
        if not config_path:
            return
        self._config_data = QSettings(config_path, QSettings.IniFormat)
        if self._config_data.value('theme') in {theme.value for theme in NTheme}:
            self.theme = NTheme(self._config_data.value('theme'))
        else:
            self.theme = NTheme.light

    def save(self):
        """
        Save settings to config file
        """
        if not self._config_data:
            raise ValueError("The Configuration File Is Not Initialized")
        self._config_data.sync()

    def get(self, key):
        """
        Get value from config file
        Args:
            key (str): The key
        """
        if not self._config_data:
            raise ValueError("The Configuration File Is Not Initialized")
        return self._config_data.value(key)

    def set(self, key, value):
        """
        Set value from config file
        Args:
            key (str): The key
            value (str): The value
        """
        if not self._config_data:
            raise ValueError("The Configuration File Is Not Initialized")
        self._config_data.setValue(key, value)
