import pandas as pd

from libs.utils.pandas.common import get_all_file_in_folder

YELLOW_TRIP_DATA_SOURCE = "/opt/airflow/share_data/yellow_trip/source"
YELLOW_TRIP_DATA_SHARE = "/opt/airflow/share_data/yellow_trip/raw"

def ingest_yellow_trip():
    source_file_names = get_all_file_in_folder(YELLOW_TRIP_DATA_SOURCE)
    share_raw_file_names = get_all_file_in_folder(YELLOW_TRIP_DATA_SHARE)
    for file_name in source_file_names:
        if file_name not in share_raw_file_names:
            data = pd.read_parquet(f"{ YELLOW_TRIP_DATA_SOURCE }/{ file_name }", engine='pyarrow')
            data.to_parquet(f"{ YELLOW_TRIP_DATA_SHARE }/{ file_name }", engine='pyarrow', compression='snappy')

if __name__ == "__main__":
    ingest_yellow_trip()