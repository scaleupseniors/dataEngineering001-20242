from typing import Callable

from pyspark.sql import DataFrame
from pyspark.sql.streaming import DataStreamWriter


class LoadStage:
    """
    A stage for loading data to a target location using a custom load function.
    """
    def __init__(self, data_load_path: str):
        """
        Initialize the LoadStage with the target data load path.

        :param data_load_path: The path where data will be loaded.
        :type data_load_path: str
        """
        self._data_load_path = data_load_path

    def load_2_target(self, data: DataFrame, load_function: Callable) -> DataStreamWriter:
        """
        Load data to the target location using a custom load function.

        This method configures a streaming DataFrame to write data to the target location
        using the specified load function.

        :param data: The DataFrame containing the data to be loaded.
        :type data: DataFrame
        :param load_function: The function used to process and load each batch of data.
        :type load_function: Callable
        :return: The streaming DataStreamWriter configured to load data to the target location.
        :rtype: DataStreamWriter
        :raises LoadStageError: If an error occurs during data loading.
        """
        try:
            return (
                data
                .writeStream
                .format("parquet")
                .option("checkpointLocation", f"{self._data_load_path}/_checkpoint")
                .trigger(once=True)
                .foreachBatch(load_function)
            )
        except Exception as e:
            raise Exception(f"The following exception has occurred while trying to load data into {self._data_load_path}", e)