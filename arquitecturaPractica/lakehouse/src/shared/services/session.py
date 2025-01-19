from pyspark.sql import SparkSession


class Session:
    """
    A utility class for managing a SparkSession instance.
    """

    _session = None

    @classmethod
    def _initialize(cls):
        """
        Initialize the SparkSession if it hasn't been created yet.

        :return: None
        """
        if cls._session is None:
            cls._session = (
                SparkSession
                .builder
                .getOrCreate()
            )

    @classmethod
    def get(cls) -> SparkSession:
        """
        Get the shared SparkSession instance.

        If the SparkSession hasn't been created yet, it will be initialized.

        :return: The shared SparkSession instance.
        :rtype: SparkSession
        """
        cls._initialize()
        return cls._session