from libs.etl_yellow_trip.constant import YELLOW_TRIP_DATA_STG, DWH_YELLOW_TRIP_TABLE_NAME
from libs.postgre.execute import duckdb_insert_parquet_to_table


def yellow_trip_load():
    duckdb_insert_parquet_to_table(DWH_YELLOW_TRIP_TABLE_NAME, f"{YELLOW_TRIP_DATA_STG}/*.parquet")