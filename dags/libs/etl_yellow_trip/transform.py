import pandas as pd

from libs.pandas.transform import tf_text_null_to_none, tf_datetime_to_date_time
from libs.utils.common import get_all_file_in_folder, path_create_folder
from libs.etl_yellow_trip.constant import YELLOW_TRIP_DATA_RAW, YELLOW_TRIP_DATA_STG, COLUMN_RENAME_MAP


def clean_data(data):
    tf_text_null_to_none(data)

    tf_datetime_to_date_time(data, "tpep_pickup_datetime", True)
    tf_datetime_to_date_time(data, "tpep_dropoff_datetime", True)
    data.drop(columns=['tpep_pickup_datetime', 'tpep_dropoff_datetime'], inplace=True)

    data.rename(columns=COLUMN_RENAME_MAP, inplace=True)

def yellow_trip_transform():
    path_create_folder(YELLOW_TRIP_DATA_RAW)
    path_create_folder(YELLOW_TRIP_DATA_STG)

    raw_file_names = get_all_file_in_folder(YELLOW_TRIP_DATA_RAW)
    stg_file_names = get_all_file_in_folder(YELLOW_TRIP_DATA_STG)
    for file_name in raw_file_names:
        if file_name not in stg_file_names:
            data = pd.read_parquet(f"{ YELLOW_TRIP_DATA_RAW }/{ file_name }", engine='pyarrow')

            clean_data(data)

            data.to_parquet(f"{ YELLOW_TRIP_DATA_STG }/{ file_name }", engine='pyarrow', compression='snappy')
