import pandas as pd
import psycopg2

# Ánh xạ kiểu dữ liệu Pandas → PostgreSQL
def map_dtype(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        if dtype == "int64":
            return "BIGINT"
        else:
            return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "TIMESTAMP"
    else:
        return "TEXT"

def parquet_to_sql(df):
    columns = []
    for col in df.columns:
        pg_type = map_dtype(df[col].dtype)
        columns.append(f'"{col}" {pg_type}')
    schema = ",\n    ".join(columns)

    return schema


def generate_create_table_sql(df, tb_name, added_schema=''):
    schema = parquet_to_sql(df)

    return f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        {added_schema}
        {schema}
    );"""


def generate_create_table_sql_with_pk_increasement(df, tb_name, pk_name):
    return generate_create_table_sql(df, tb_name, f"{pk_name} SERIAL PRIMARY KEY,")
