YELLOW_TRIP_DATA_FOLDER = "/opt/airflow/share_data/yellow_trip"
YELLOW_TRIP_DATA_SOURCE = f"{YELLOW_TRIP_DATA_FOLDER}/source"
YELLOW_TRIP_DATA_RAW = f"/{YELLOW_TRIP_DATA_FOLDER}/raw"
YELLOW_TRIP_DATA_STG = f"/{YELLOW_TRIP_DATA_FOLDER}/stg"
YELLOW_TRIP_DATA_LOADED = f"/{YELLOW_TRIP_DATA_FOLDER}/loaded.txt"

DWH_YELLOW_TRIP_TABLE_NAME = "yellow_trips"

COLUMN_RENAME_MAP = {
    'VendorID': 'vendor_id',
    'RatecodeID': 'rate_code_id',
    'PULocationID': 'pu_location_id',
    'DOLocationID': 'do_location_id',
    'Airport_fee': 'airport_fee',
}