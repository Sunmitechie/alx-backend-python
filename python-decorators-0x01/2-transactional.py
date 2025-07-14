#!/usr/bin/python3
import sqlite3
import functools


def with_db_connection(func):
    """
    Decorator that opens a SQLite DB connection, passes it to the function,
    and ensures it is closed afterwards.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper


def transactional(func):
    """
    Decorator that manages a transaction.
    Commits if function succeeds, rolls back if it fails.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()  # ✅ Commit on success
            return result
        except Exception as e:
            conn.rollback()  # ❌ Rollback on failure
            print(f"Transaction failed: {e}")
            raise
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


# ✅ Update user safely with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
