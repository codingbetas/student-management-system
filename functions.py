import sqlite3

def insert(name, age, course, grade):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO students VALUES (NULL, ?, ?, ?, ?)", (name, age, course, grade))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(id):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id=?", (id,))
    row = cur.fetchone()
    conn.close()
    return row

def update(id, name, age, course, grade):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET name=?, age=?, course=?, grade=? WHERE id=?", (name, age, course, grade, id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
