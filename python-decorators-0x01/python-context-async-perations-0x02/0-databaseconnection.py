#!/usr/bin/python3
import sqlite3


class DatabaseConnection:
    """
    Custom context manager for handling SQLite DB connections.
    """
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection  # This is passed to the `as conn` part

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()  # Always close DB
