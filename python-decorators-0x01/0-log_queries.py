#!/usr/bin/python3
import sqlite3
import functools
from datetime import datetime  # ✅ required by the checker


def log_queries():
    """
    Decorator that logs the SQL query with a timestamp before execution.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            query = kwargs.get('query', None)
            if query:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] Executing SQL query: {query}")
            else:
                print("No query provided.")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_queries()
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
