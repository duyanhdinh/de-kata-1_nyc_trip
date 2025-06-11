import os
import psycopg2
from sqlalchemy import create_engine

def get_dwh_env():
    return {
        "host": os.environ.get("DWH_HOST", ""),
        "port": os.environ.get("DWH_PORT", '5432'),
        "dbname": os.environ.get("DWH_DBNAME", ""),
        "user": os.environ.get("DWH_USER", ""),
        "password": os.environ.get("DWH_PASSWORD", "")
    }

def pg_url(ext=''):
    env = get_dwh_env()
    return f"postgresql{ext}://{env['user']}:{env['password']}@{env['host']}:{env['port']}/{env['dbname']}"

def pg_url_w_psy():
    return pg_url('+psycopg2')

def psy_connect():
    conn = psycopg2.connect(**get_dwh_env())

    return conn

def get_engine():
    return create_engine(pg_url_w_psy())

