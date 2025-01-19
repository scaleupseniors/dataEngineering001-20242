from typing import Callable

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.window import Window
from pyspark.sql.functions import (
    monotonically_increasing_id,
    row_number,
    collect_list
)
from numpy import fft, array


class TransformStage:
    """
    A stage for transforming data and optimizing tables in Spark.
    """
    def __init__(self, spark_session: SparkSession):
        """
        Initialize the TransformStage with the SparkSession.

        :param spark_session: The SparkSession instance.
        :type spark_session: SparkSession
        """
        self._spark_session = spark_session

    def get_frequencies(self,
                        batch: DataFrame,
                        columns_2_transform: None | list = None) -> DataFrame:
        """
        Perform Inverse Fast Fourier Transform (IFFT) on specified columns of the input DataFrame.

        :param batch: Input DataFrame containing the data to transform.
        :param columns_2_transform: Optional list of column names to apply FFT.
                                    If None, default columns ["vib_x", "vib_y", "vib_z"] will be used.
        :return: DataFrame with Fourier Transform applied to specified columns.
        """
        def generate_index(dataframe: DataFrame):
            """
            Generate an index column starting from 1 for the given DataFrame.

            :param dataframe: Input DataFrame.
            :return: DataFrame with an additional 'index' column starting from 1.
            """
            dataframe = dataframe.withColumn("counter", monotonically_increasing_id())
            window = Window.orderBy("counter")
            return dataframe.withColumn("index", row_number().over(window))\
                .drop("counter")

        def compute_ifft(column_values: list) -> list:
            """
            Compute Inverse Fast Fourier Transform (IFFT) on a list of complex numbers.

            :param column_values: List of complex values to compute IFFT.
            :return: List of real values resulting from IFFT.
            """
            ifft_values = fft.ifft(array(column_values))
            return ifft_values.real.tolist()

        if batch.isEmpty():
            raise Exception("The given batch happens to be empty.")

        columns_2_transform = ["vib_x", "vib_y", "vib_z"] if columns_2_transform is None \
            else columns_2_transform

        batch = generate_index(batch)

        for column in columns_2_transform:
            batch_column_values: list = batch.select(collect_list(column)).first()[0]
            ifft_col_values: list = compute_ifft(batch_column_values)
            ifft_col_values_parallelized = self._spark_session.sparkContext.parallelize(
                [(value, ) for value in ifft_col_values]
            )
            col_name = f"freq_{column}"
            ifft_col: DataFrame = ifft_col_values_parallelized.toDF([col_name])
            ifft_col = generate_index(ifft_col)
            batch = batch.join(ifft_col, "index", "inner")

        return batch.drop("index")

    def _load(self, load_target: str, load_source: str):
        """
        Load data from a source table into a target table.

        :param load_target: The name of the target table.
        :type load_target: str
        :param load_source: The name of the source table.
        :type load_source: str
        """
        self._spark_session.sql(f"""
            INSERT INTO default.{load_target}
            SELECT * FROM global_temp.{load_source}
        """)

    def _optimize(self, load_target: str):
        """
        Optimize a table by performing VACUUM and OPTIMIZE operations.

        :param load_target: The name of the table to optimize.
        :type load_target: str
        """
        self._spark_session.sql(f"OPTIMIZE default.{load_target}")
        self._spark_session.sql(f"VACUUM default.{load_target} RETAIN 0 HOURS")

    def get_transformations(self, load_target: str) -> Callable:
        """
        Get a transformation function that can be applied to DataFrame batches.

        :param load_target: The name of the target table for loading transformed data.
        :type load_target: str
        :return: A transformation function accepting a DataFrame batch and an ignored argument.
        :rtype: Callable
        """
        def transformations_flux(batch: DataFrame, _) -> None:
            """
            Apply transformations to a DataFrame batch.

            This function creates a global temporary view from the DataFrame batch,
            loads the transformed data into the target table, and optimizes the target table.

            :param batch: The DataFrame batch to transform.
            :type batch: DataFrame
            :param _: Ignored argument (not used in the transformation function).
            :return: None
            """
            batch.show(10)
            batch = self.get_frequencies(batch)
            batch.createOrReplaceGlobalTempView("source")
            self._load(load_target, "source")
            self._optimize(load_target)

        return transformations_flux