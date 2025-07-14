#!/usr/bin/python3
import time
import sqlite3
import functools

query_cache = {}  # Global cache dictionary


def with_db_connection(func):
    """
    Opens SQLite DB connection, injects it, and closes it automatically.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper


def cache_query(func):
    """
    Decorator that caches DB query results based on the query string.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get('query')
        if query in query_cache:
            print(f"✅ Returning cached result for query: {query}")
            return query_cache[query]
        else:
            result = func(conn, *args, **kwargs)
            query_cache[query] = result
            print(f"🆕 Query executed and cached: {query}")
            return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# 🔁 First call – runs and caches the query
users = fetch_users_with_cache(query="SELECT * FROM users")

# ✅ Second call – uses cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
