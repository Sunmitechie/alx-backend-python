#!/usr/bin/python3
import asyncio
import aiosqlite


async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        cursor = await db.execute("SELECT * FROM users")
        rows = await cursor.fetchall()
        print("\n✅ All Users:")
        for row in rows:
            print(row)


async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        rows = await cursor.fetchall()
        print("\n📌 Users older than 40:")
        for row in rows:
            print(row)


async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )


# 🔁 Run the coroutines concurrently
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
# This script demonstrates how to use asyncio and aiosqlite to fetch data concurrently from a SQLite database.