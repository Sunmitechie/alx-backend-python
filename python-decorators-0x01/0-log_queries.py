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
                print(f"Executing query: {query}")