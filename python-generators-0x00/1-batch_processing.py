#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error


def stream_users_in_batches(batch_size):
    """
    Generator that yields users in batches from the user_data table.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # 🔁 Update credentials if needed
            password="password",
            database="ALX_prodev"
        )

        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM user_data")
        total_rows = cursor.fetchone()[0]

        offset = 0
        while offset < total_rows:
            cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))
            rows = cursor.fetchall()
            columns = cursor.column_names
            if not rows:
                break
            yield [dict(zip(columns, row)) for row in rows]
            offset += batch_size

        cursor.close()
        connection.close()

    except Error as e:
        print(f"Error: {e}")
        return


def batch_processing(batch_size):
    """
    Process each batch and print users whose age > 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if float(user['age']) > 25:
                print(user)
