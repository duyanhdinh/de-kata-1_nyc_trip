import pandas as pd
import os

from libs.utils.pandas.transform import tf_text_null_to_none, tf_datetime_to_date_time
from libs.utils.pandas.common import get_all_file_in_folder

YELLOW_TRIP_DATA_RAW = "/opt/airflow/share_data/yellow_trip/raw"
YELLOW_TRIP_DATA_STG = "/opt/airflow/share_data/yellow_trip/stg"

def yellow_trip_source_files():
    file_names = [f for f in os.listdir(YELLOW_TRIP_DATA_RAW) if os.path.isfile(os.path.join(YELLOW_TRIP_DATA_RAW, f))]
    return file_names

def clean_data(data):
    tf_text_null_to_none(data)
    tf_datetime_to_date_time(data, "tpep_pickup_datetime", True)
    tf_datetime_to_date_time(data, "tpep_dropoff_datetime", True)

    data.drop(columns=['tpep_pickup_datetime', 'tpep_dropoff_datetime'], inplace=True)

def transform_yellow_trip():
    raw_file_names = get_all_file_in_folder(YELLOW_TRIP_DATA_RAW)
    stg_file_names = get_all_file_in_folder(YELLOW_TRIP_DATA_STG)
    for file_name in raw_file_names:
        if file_name not in stg_file_names:
            data = pd.read_parquet(f"{ YELLOW_TRIP_DATA_RAW }/{ file_name }", engine='pyarrow')

            clean_data(data)

            data.to_parquet(f"{ YELLOW_TRIP_DATA_STG }/{ file_name }", engine='pyarrow', compression='snappy')
