#!/usr/bin/python3
import sqlite3


class ExecuteQuery:
    """
    Custom reusable context manager to execute a query
    and manage the DB connection lifecycle.
    """

    def __init__(self, query, params=None, db_name="users.db"):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.connection = None
        self.results = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        cursor = self.connection.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
