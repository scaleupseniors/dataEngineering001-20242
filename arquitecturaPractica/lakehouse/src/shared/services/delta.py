import copy

from pyspark.sql.types import StructType
from pyspark.sql.session import SparkSession


class DeltaTable:
    """
    A utility class for managing Delta tables using SparkSession.
    """
    def __init__(self, spark_session: SparkSession):
        """
        Initialize the DeltaTable with a SparkSession.

        :param spark_session: The SparkSession to use for executing SQL queries.
        :type spark_session: SparkSession
        """
        self._spark_session = spark_session

    @staticmethod
    def _get_table_creation_query(table_name: str,
                                  data_schema: StructType,
                                  table_path: str) -> str:
        """
        Generate the SQL query string for creating a Delta table.

        :param table_name: The name of the Delta table.
        :type table_name: str
        :param data_schema: The schema of the data to be stored in the Delta table.
        :type data_schema: StructType
        :param table_path: The path where the Delta table will be stored.
        :type table_path: str
        :return: The SQL query string for creating the Delta table.
        :rtype: str
        """
        def gen_table_query(schema_fields: list, table_query: str = ""):
            """
            Generate the table schema definition portion of the SQL query.

            :param schema_fields: The list of schema fields.
            :type schema_fields: list
            :param table_query: The current table creation query string.
            :type table_query: str
            :return: The updated table creation query string.
            :rtype: str
            """
            if len(schema_fields) == 0:
                return table_query
            table_query += (f"{schema_fields[0].name} {(schema_fields[0].dataType.simpleString()).upper()}, \n"
                            if len(schema_fields) > 1
                            else
                            f"{schema_fields[0].name} {(schema_fields[0].dataType.simpleString()).upper()}")
            schema_fields.pop(0)
            return gen_table_query(schema_fields, table_query)

        return f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {gen_table_query((copy.deepcopy(data_schema)).fields)}
            )
            USING DELTA
            LOCATION '{table_path}'
        """

    def create(self,
               table_name: str,
               data_schema: StructType,
               table_path: str):
        """
        Create a Delta table using the provided table name, data schema, and table path.

        :param table_name: The name of the Delta table to create.
        :type table_name: str
        :param data_schema: The schema of the data to be stored in the Delta table.
        :type data_schema: StructType
        :param table_path: The path where the Delta table will be stored.
        :type table_path: str
        :return: None
        """
        self._spark_session.sql(
            self._get_table_creation_query(
                table_name=table_name,
                data_schema=data_schema,
                table_path=table_path
            )
        )
