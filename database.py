import sqlite3

def connect():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT,
            grade TEXT
        )
    """)
    conn.commit()
    conn.close()
