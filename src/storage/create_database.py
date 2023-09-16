import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from src.config import (
    DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
)


def close(conn, cursor):
    cursor.close()
    conn.close()


def create_database():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
    except Exception as e:
        print(f"Unable to connect to server!\n{e}")
    else:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        try:
            sql = f"CREATE DATABASE {DB_NAME}"
            cursor.execute(sql)
            close(conn, cursor)
            print("Database created!")
        except Exception as e:
            close(conn, cursor)
            print(e)


def create_tables():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    except Exception as e:
        print(f"Unable to connect to database!\n{e}")
    else:
        cursor = conn.cursor()
        with conn:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS project (
                id BIGSERIAL NOT NULL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                date_of_creation DATE NOT NULL);
            """)
        print("Table of projects set up!")

        with conn:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS contract (
                id BIGSERIAL NOT NULL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                date_of_creation DATE NOT NULL,
                date_of_approval DATE,
                status VARCHAR(10) NOT NULL DEFAULT 'draft',
                project_id BIGINT REFERENCES project (id));
            """)
        print("Table of contracts set up!")

        close(conn, cursor)
