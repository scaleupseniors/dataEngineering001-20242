from abc import ABC, abstractmethod


class StorageInterface(ABC):
    """
    An abstract base class defining the interface for storage operations.
    """
    @abstractmethod
    def check_existing_bucket(self, storage_path: str) -> 'StorageInterface':
        """
        Check if a bucket or container exists at the given storage path.

        :param storage_path: The path to the storage bucket or container.
        :type storage_path: str
        :return: An instance of StorageInterface representing the result.
        :rtype: StorageInterface
        """
        pass
    
    @abstractmethod
    def check_existing_data_in_storage_path(self, storage_path: str) -> 'StorageInterface':
        """
        Check if data exists within the specified storage path.

        :param storage_path: The path to the storage location.
        :type storage_path: str
        :return: An instance of StorageInterface representing the result.
        :rtype: StorageInterface
        """
        pass
