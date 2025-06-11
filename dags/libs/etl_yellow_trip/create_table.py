import pandas as pd
from libs.etl_yellow_trip.constant import YELLOW_TRIP_DATA_STG, DWH_YELLOW_TRIP_TABLE_NAME
from libs.utils.common import get_all_file_in_folder
from libs.postgre.generate import generate_create_table_sql
from libs.postgre.execute import commit_table_schema


def yellow_trip_create_table():
    stg_file_names = get_all_file_in_folder(YELLOW_TRIP_DATA_STG)
    df = pd.read_parquet(f"{YELLOW_TRIP_DATA_STG}/{stg_file_names[0]}", engine='pyarrow')

    schema = generate_create_table_sql(df, DWH_YELLOW_TRIP_TABLE_NAME)
    commit_table_schema(schema)
