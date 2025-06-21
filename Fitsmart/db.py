import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

load_dotenv()

dbconfig = {
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASS"),
    "host": os.getenv("MYSQL_HOST"),
    "database": os.getenv("MYSQL_DB")
}

pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **dbconfig)

def query_db(query, params=None, fetchone=False, commit=False):
    conn = pool.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params or [])
    if commit:
        conn.commit()
    result = cursor.fetchone() if fetchone else cursor.fetchall()
    cursor.close()
    conn.close()
    return result
