import json
from datetime import datetime
import psycopg2
import redis
from psycopg2 import Error
import os


user = os.environ["USERNAME"]
password = os.environ["PASSWORD"]
port_postgres = os.environ["PORT_POSTGRES"]
host_postgres = os.environ["HOSTNAME"]
database = os.environ["DB_NAME"]
port_redis = os.environ["PORT_REDIS"]
hostname_redis = os.environ["HOSTNAME_REDIS"]

try:
    conn = psycopg2.connect(
        user=user,
        password=password,
        port=port_postgres,
        host=host_postgres,
        database=database,
    )

    cur = conn.cursor()

    create_table = """CREATE TABLE IF NOT EXISTS information (
                    id SERIAL PRIMARY KEY,
                    user_id INT NOT NULL,
                    timestamp TIMESTAMP(0),
                    gender VARCHAR(255),
                    age INT,
                    mark INT,
                    diese VARCHAR(255));"""
    cur.execute(create_table)
    conn.commit()
    print("Table created successfully!")

    insert_query = """INSERT INTO information (user_id, timestamp, gender, age, mark, diese)
                    VALUES (%s, %s, %s, %s, %s, %s);"""

    r = redis.StrictRedis(host=hostname_redis, port=port_redis)

    while True:
        data = r.blpop("information")
        data_to_json = json.loads(data[1])
        record_value = (
            data_to_json["user_id"],
            data_to_json["timestamp"],
            data_to_json["gender"],
            data_to_json["age"],
            data_to_json["mark"],
            data_to_json["diese"],
        )
        print(data_to_json)
        cur.execute(insert_query, record_value)

        conn.commit()
        print(f"{datetime.now()} - Inserted To DB!")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
