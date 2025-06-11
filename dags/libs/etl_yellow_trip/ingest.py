import pandas as pd

from libs.utils.common import get_all_file_in_folder, path_create_folder, load_file_list_from_txt
from libs.etl_yellow_trip.constant import YELLOW_TRIP_DATA_SOURCE, YELLOW_TRIP_DATA_RAW, YELLOW_TRIP_DATA_LOADED


def yellow_trip_ingest():
    path_create_folder(YELLOW_TRIP_DATA_RAW)

    source_file_names = get_all_file_in_folder(YELLOW_TRIP_DATA_SOURCE)
    share_raw_file_names = get_all_file_in_folder(YELLOW_TRIP_DATA_RAW)
    loaded_file_names = load_file_list_from_txt(YELLOW_TRIP_DATA_LOADED)
    for file_name in source_file_names:
        if file_name not in share_raw_file_names + loaded_file_names:
            data = pd.read_parquet(f"{ YELLOW_TRIP_DATA_SOURCE }/{ file_name }", engine='pyarrow')
            data.to_parquet(f"{ YELLOW_TRIP_DATA_RAW }/{ file_name }", engine='pyarrow', compression='snappy')

if __name__ == "__main__":
    yellow_trip_ingest()