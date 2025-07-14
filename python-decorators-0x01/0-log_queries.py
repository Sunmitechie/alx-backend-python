#!/usr/bin/python3
import sqlite3
import functools


def log_queries():
    """
    Decorator that logs the SQL query before it's executed.
    Assumes the decorated function has a 'query' keyword argument.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            query = kwargs.get('query', None)
            if query:
                print(f"Executing SQL query: {query}")
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
