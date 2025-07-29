import os
import sqlite3
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

conn = sqlite3.connect(":memory:", check_same_thread=False)
conn.execute(
    "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)"
)

USERNAME = os.environ.get("APP_USERNAME")
PASSWORD = os.environ.get("APP_PASSWORD")

if USERNAME and PASSWORD:
    hashed = pwd_context.hash(PASSWORD)
    conn.execute(
        "INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)",
        (USERNAME, hashed),
    )
    conn.commit()


def verify_user(username: str, password: str) -> bool:
    cur = conn.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    if row:
        return pwd_context.verify(password, row[0])
    return False
