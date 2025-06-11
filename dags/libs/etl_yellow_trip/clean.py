from libs.utils.common import get_all_file_in_folder, path_create_folder
from libs.etl_yellow_trip.constant import YELLOW_TRIP_DATA_SOURCE, YELLOW_TRIP_DATA_RAW, YELLOW_TRIP_DATA_STG, YELLOW_TRIP_DATA_LOADED
from libs.utils.common import clean_folder, append_file_list


def yellow_trip_clean():
    file_names = get_all_file_in_folder(YELLOW_TRIP_DATA_STG)
    append_file_list(file_names, YELLOW_TRIP_DATA_LOADED)

    clean_folder(YELLOW_TRIP_DATA_RAW)
    clean_folder(YELLOW_TRIP_DATA_STG)