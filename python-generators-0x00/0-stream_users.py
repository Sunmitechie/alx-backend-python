#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error


def stream_users():
    """
    Generator that streams rows from user_data table one by one.
    Yields each row as a dictionary.
    """
    try:
        # Connect to ALX_prodev database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # 🔁 Use your own MySQL username
            password="password",   # 🔁 Use your own MySQL password
            database="ALX_prodev"
        )

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")

        columns = cursor.column_names  # Get column names

        for row in cursor:
            # Build dict: {'user_id': '...', 'name': '...', ...}
            yield dict(zip(columns, row))

        cursor.close()
        connection.close()

    except Error as e:
        print(f"Error: {e}")
        return
