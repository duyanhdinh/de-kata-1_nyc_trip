from sqlalchemy import text
import duckdb

from libs.postgre.connect import psy_connect, pg_url_w_psy, pg_url, get_dwh_env

def engine_exe(engine, tb_name, query):
    with engine.connect() as conn:
        conn.execute(text(f"""
            ALTER TABLE {tb_name}
            {query}
        """))

def add_pk_auto_increase(engine, tb_name, pk_name):
    engine_exe(engine, tb_name, f"ADD COLUMN {pk_name} SERIAL PRIMARY KEY;")

def commit_table_schema(tb_schema):
    conn = psy_connect()
    cur = conn.cursor()

    cur.execute(tb_schema)
    conn.commit()

    cur.close()
    conn.close()

def duckdb_insert_parquet_to_table(tb_name, parquet_path):
    env = get_dwh_env()
    query = f"""
        ATTACH 'dbname={env['dbname']} user={env['user']} password={env['password']} host={env['host']} port={env['port']}' AS postgres_db (TYPE postgres);
        INSERT INTO postgres_db.{tb_name}
        SELECT * FROM parquet_scan('{parquet_path}');
    """

    # connect & exec
    duckdb.sql("INSTALL postgres; LOAD postgres;")
    duckdb.sql(query)