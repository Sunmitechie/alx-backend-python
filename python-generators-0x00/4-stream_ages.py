#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error


def stream_user_ages():
    """
    Generator that yields user ages one by one from the database.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # 🔁 Use your DB credentials
            password="password",
            database="ALX_prodev"
        )

        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        for row in cursor:
            yield float(row[0])  # age is the only column returned

        cursor.close()
        connection.close()

    except Error as e:
        print(f"Database error: {e}")
        return


def calculate_average_age():
    """
    Uses the generator to calculate the average age without
    loading all ages into memory.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count > 0:
        average = total_age / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No user data found.")
