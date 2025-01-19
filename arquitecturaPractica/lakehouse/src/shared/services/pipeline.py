from typing import Union
from shared.interfaces.storage import StorageInterface
from shared.services.delta import DeltaTable
from shared.stages import (
    extract,
    transform,
    load
)

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType


class Pipeline:
    """
    A class representing an ETL pipeline.
    """
    def __init__(self, 
                 spark_session: SparkSession,
                 storage_client: StorageInterface):
        """
        Initialize the Pipeline with required components.

        :param spark_session: The SparkSession instance.
        :type spark_session: SparkSession
        :param storage_client: The storage client implementing StorageInterface.
        :type storage_client: StorageInterface
        """
        self._spark_session = spark_session
        self._storage_client = storage_client
        self._extract_stage: Union[None, extract.ExtractStage] = None
        self._transform_stage: Union[None, transform.TransformStage] = None
        self._load_stage: Union[None, load.LoadStage] = None

    def build_delta_table(self,
                          table_name: str,
                          table_data_schema: StructType,
                          table_path: str) -> 'Pipeline':
        """
        Build a Delta table.

        :param table_name: The name of the Delta table to create.
        :type table_name: str
        :param table_data_schema: The schema of the Delta table to be created.
        :type table_data_schema: StructType
        :param table_path: The path where the Delta table will be stored.
        :type table_path: str
        :return: The Pipeline instance.
        :rtype: Pipeline
        :raises NotExistingDeltaTableError: If the Delta table doesn't exist after creation.
        """
        DeltaTable(self._spark_session).create(table_name, table_data_schema, table_path)
        if not self._spark_session.catalog.tableExists(table_name):
            raise Exception(
                "The Delta Table in spark catalog path 'default.{table_name}' couldn't be found")
        return self

    def build_extract_stage(self,
                            input_data_schema: StructType,
                            data_extraction_path: str) -> 'Pipeline':
        """
        Build the extract stage of the pipeline.

        :param input_data_schema: The schema of the data to be processed.
        :type input_data_schema: StructType
        :param data_extraction_path: The path from which to extract data.
        :type data_extraction_path: str
        :return: The Pipeline instance.
        :rtype: Pipeline
        """
        def check_pre_conditions(storage_path: str):
            """
            Checks if the specified storage path has an existing bucket and existing data
            using the storage client.

            :param storage_path: The storage path to check.
            :type storage_path: str
            """
            (
                self._storage_client
                .check_existing_bucket(storage_path)
                .check_existing_data_in_storage_path(storage_path)
            )

        check_pre_conditions(storage_path=data_extraction_path)
        self._extract_stage = extract.ExtractStage(
            self._spark_session,
            schema=input_data_schema,
            data_extraction_path=data_extraction_path
        )
        return self

    def build_transform_stage(self) -> 'Pipeline':
        """
        Build the transform stage of the pipeline.

        :return: The Pipeline instance.
        :rtype: Pipeline
        """
        self._transform_stage = transform.TransformStage(self._spark_session)
        return self

    def build_load_stage(self, data_load_path: str):
        """
        Build the load stage of the pipeline.

        :param data_load_path: The path to which transformed data will be loaded.
        :type data_load_path: str
        :return: The Pipeline instance.
        :rtype: Pipeline
        """
        def check_pre_conditions(storage_path: str):
            """
            Checks if the specified storage path has an existing bucket
            using the instance's storage client.

            :param storage_path: The storage path to check.
            :type storage_path: str
            """
            (
             self._storage_client
             .check_existing_bucket(storage_path)
            )

        check_pre_conditions(storage_path=data_load_path)
        self._load_stage = load.LoadStage(data_load_path)
        return self

    def _check_build_stages(self) -> None:
        """
        Check if all required stages have been built.

        :raises MissingExtractStageError: If the extract stage is missing.
        :raises MissingTransformStageError: If the transform stage is missing.
        :raises MissingLoadStageError: If the load stage is missing.
        """
        if self._extract_stage is None:
            raise Exception("")
        elif self._transform_stage is None:
            raise Exception("")
        elif self._load_stage is None:
            raise Exception("")

    def execute(self, load_target: str):
        """
        Execute the ETL pipeline.

        :param load_target: The name of the Delta table.
        :type load_target: str
        """
        self._check_build_stages()
        source_data = self._extract_stage.extract_from_source()
        transform_function = self._transform_stage.get_transformations(load_target)
        load_2_target = self._load_stage.load_2_target(source_data, transform_function)
        load_2_target.start().awaitTermination()