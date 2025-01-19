from shared.interfaces.config import ConfigInterface

from dynaconf import Dynaconf
from dynaconf.base import LazySettings


class Config(ConfigInterface):
    """
    Implementation of ConfigInterface using Dynaconf for configuration management.
    """
    _config: None | LazySettings = None

    @classmethod
    def get(cls, settings_file_name: str = "config.yaml") -> LazySettings:
        """
        Get the configuration object.

        This method retrieves or initializes the configuration object using Dynaconf.
        If the configuration object has not been initialized, it will be created with the specified settings file.

        :param settings_file_name: The name of the settings file to load.
        :type settings_file_name: str
        :return: The Dynaconf LazySettings object representing the configuration.
        :rtype: LazySettings
        :raises EmptyConfigsError: If the configuration file couldn't be found or is empty.
        """
        if cls._config is None:
            cls._config = Dynaconf(settings_files=[settings_file_name])

        if len(cls._config.to_dict()) <= 0:
            raise Exception("The configuration file couldn't be found or is empty.")
        return cls._config
