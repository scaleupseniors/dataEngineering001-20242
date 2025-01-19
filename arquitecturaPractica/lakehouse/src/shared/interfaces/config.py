from abc import ABC, abstractmethod

from dynaconf import Dynaconf


class ConfigInterface(ABC):
    """
    An abstract base class defining the interface for configuration operations.
    """
    @classmethod
    @abstractmethod
    def get(cls) -> Dynaconf:
        """
        Retrieve the configuration object.

        This method should be implemented to return a configuration object
        compatible with Dynaconf.

        :return: A configuration object.
        :rtype: Dynaconf
        """
        ...
