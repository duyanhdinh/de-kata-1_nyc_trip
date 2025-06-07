import pandas as pd

def tf_text_null_to_none(data):
    data.replace('', None, inplace=True)

def tf_datetime_to_date_time(data, col, get_time=False, get_second=False):
    date = pd.to_datetime(data[col], errors='coerce')
    data[f"{col}_date"] = date.dt.strftime("%Y%m%d")

    if get_time:
        time_format = "%H%M%S" if get_second else "%H%M"
        data[f"{col}_time"] = date.dt.strftime(time_format)