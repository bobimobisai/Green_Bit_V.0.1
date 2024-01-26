import psycopg
from config import db_user, db_pass

# db config

db_name = "postgres"
username = db_user
password = db_pass
host = "127.0.0.1"
port = 5432


# sample requests
create_table = """
            CREATE TABLE test (
                id serial PRIMARY KEY,
                num INT,
                data VARCHAR)
            """
enter_data = "INSERT INTO test (num, data) VALUES (%s, %s)"

get_data = "SELECT * FROM test"

# db conection

with psycopg.connect(
    dbname=db_name, user=username, password=password, port=port, host=host
) as conn:
    with conn.cursor() as cur:
        cur.execute(get_data)
        res = cur.fetchone()
        print(res)
