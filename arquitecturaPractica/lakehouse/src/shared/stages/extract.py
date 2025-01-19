from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql import DataFrame


class ExtractStage:
    """
    A stage for extracting streaming data from a specified source path.
    """
    def __init__(self,
                 spark_session: SparkSession,
                 schema: StructType,
                 data_extraction_path: str):
        """
        Initialize the ExtractStage with required parameters.

        :param spark_session: The SparkSession instance.
        :type spark_session: SparkSession
        :param schema: The schema to apply to the data during extraction.
        :type schema: StructType
        :param data_extraction_path: The path from which to extract streaming data.
        :type data_extraction_path: str
        """
        self._spark_session = spark_session
        self._schema = schema
        self._data_extraction_path = data_extraction_path

    def extract_from_source(self) -> DataFrame:
        """
        Extract streaming data from the specified source path.

        This method reads streaming data from the specified path using the configured schema.

        :return: The DataFrame containing the extracted streaming data.
        :rtype: DataFrame
        :raises ExtractStageError: If an error occurs during data extraction.
        """
        try:
            return (
                self._spark_session
                .readStream
                .option("sep", ";")
                .option("header", "true")
                .schema(self._schema)
                .csv(self._data_extraction_path)
            )
        except Exception as e:
            raise Exception(f"The following exception has occurred while trying to extract data from {self._data_extraction_path}", e)