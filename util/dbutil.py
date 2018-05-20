import sqlite3
import sys


class DbUtil:
    """Utility class to connect to DB."""

    def __int__(self):
        print("Default - DBUtil")

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.con_cursor = self.connection.cursor()

    def save_query_to_db(self, query):
        self.con_cursor.execute(query)
        self.connection.commit()
        print("table created")

    def execute_query(self, query):
        self.con_cursor.execute(query)

    def execute_dynamic_query(self, query, *args):

        self.con_cursor.execute(query, args)


    def close_connection(self):
        self.connection.close()

    def fetch_one(self):
        return self.con_cursor.fetchone()

    def fetch_all(self):
        return self.con_cursor.fetchall()
