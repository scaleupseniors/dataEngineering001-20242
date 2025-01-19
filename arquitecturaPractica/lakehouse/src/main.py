from shared.services.config import Config
from shared.services.session import Session
from shared.services.google_storage import GoogleStorage
from shared.services.pipeline import Pipeline

from pyspark.sql.types import (
    StructType,
    StringType,
    FloatType
)

INPUT_DATA_SCHEMA = (
        StructType()
        .add("time", FloatType())
        .add("vib_x", FloatType())
        .add("vib_y", FloatType())
        .add("vib_z", FloatType())
        #.add("date", StringType())
        #.add("bridge_name", StringType())
        #.add("bridge_address", StringType())
        #.add("bridge_coordinates", StringType())
    )

OUTPUT_DATA_SCHEMA = (
        StructType()
        .add("time", FloatType())
        .add("vib_x", FloatType())
        .add("vib_y", FloatType())
        .add("vib_z", FloatType())
        #.add("date", StringType())
        #.add("bridge_name", StringType())
        #.add("bridge_address", StringType())
        #.add("bridge_coordinates", StringType())
        .add("freq_vib_x", FloatType())
        .add("freq_vib_y", FloatType())
        .add("freq_vib_z", FloatType())
    )

TABLE_NAME = "mobile_app"

try:
    configs = Config.get(settings_file_name="config.yml")
    session = Session.get()
    storage_client = GoogleStorage()

    pipeline = (
        Pipeline(session, storage_client)
        .build_delta_table(TABLE_NAME, OUTPUT_DATA_SCHEMA, configs.get("TRUSTED_PATH").get(TABLE_NAME))
        .build_extract_stage(INPUT_DATA_SCHEMA, data_extraction_path=configs.get("RAW_PATH").get(TABLE_NAME))
        .build_transform_stage()
        .build_load_stage(data_load_path=configs.get("TRUSTED_PATH").get(TABLE_NAME))
    )

    pipeline.execute(load_target=TABLE_NAME)
except Exception as e:
    raise Exception("An exception has occurred while trying to execute the pipeline.", e)