from shared.interfaces.storage import StorageInterface

from google.cloud import storage


class GoogleStorage(StorageInterface):
    """
    A class representing Google Cloud Storage operations.
    """
    def __init__(self, service_account_json_path: str = None):
        """
        Initialize GoogleStorage with optional service account JSON path.

        :param service_account_json_path: Path to the service account JSON file.
        :type service_account_json_path: str
        """
        self._client = (storage.Client.from_service_account_json(service_account_json_path)
                        if service_account_json_path else storage.Client())
    
    @staticmethod
    def _get_bucket_n_folders(gcs_path: str) -> tuple[str, str]:
        """
        Parse the Google Cloud Storage path into bucket name and folder(s).

        :param gcs_path: Google Cloud Storage path in the format 'gs://<bucket_name>/<folder>'
        :type gcs_path: str
        :return: A tuple containing the bucket name and folder(s) path.
        :rtype: tuple[str, str]
        """
        gcs_path = gcs_path.replace("gs://", "")
        threshold = gcs_path.find("/")
        return (
            gcs_path[0:threshold],  # bucket name
            gcs_path[threshold+1:]  # folders
        ) 

    def check_existing_bucket(self, gcs_path: str) -> 'GoogleStorage':
        """
        Check if the specified bucket exists.

        :param gcs_path: Google Cloud Storage path in the format 'gs://<bucket_name>'
        :type gcs_path: str
        :return: Self (GoogleStorage instance) if the bucket exists.
        :rtype: GoogleStorage
        :raises NotExistingBucketError: If the specified bucket doesn't exist.
        """
        try:
            bucket_name = self._get_bucket_n_folders(gcs_path)[0]
            self._client.get_bucket(bucket_name)
            return self
        except Exception as e:
            raise Exception(
                f"The specified bucket {bucket_name} couldn't be found or doesn't exist.",
                e)

    def check_existing_data_in_storage_path(self, gcs_path: str) -> 'GoogleStorage':
        """
        Check if data exists in the specified Google Cloud Storage path.

        :param gcs_path: Google Cloud Storage path in the format 'gs://<bucket_name>/<folder>'
        :type gcs_path: str
        :return: Self (GoogleStorage instance) if data exists in the specified path.
        :rtype: GoogleStorage
        :raises NotExistingStoragePathError: If the specified storage path doesn't exist.
        :raises NotExistingDataInStoragePathError: If the specified path is empty.
        """
        bucket_name, folders = self._get_bucket_n_folders(gcs_path)
        try:
            blobs = list((self._client.bucket(bucket_name)).list_blobs(prefix=folders))
        except Exception as e:
            raise Exception(
                f"The especified storage path {gcs_path} couldn't be found or doesn't exist.",
                e)
        else:
            if len(blobs) == 0:
                raise Exception(
                    f"The especified path {gcs_path} is empty.")
            return self