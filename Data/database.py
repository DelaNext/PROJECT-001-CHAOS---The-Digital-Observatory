import sqlite3

from Data.data import CPU


conn =sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cpu_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usage REAL,
    frequency REAL,
    physical_cores INTEGER,
    logical_cores INTEGER
)''')

cursor.execute("INSERT INTO cpu_usage (usage, frequency, physical_cores, logical_cores) VALUES (:usage, :frequency, :physical_cores, :logical_cores)", CPU)
conn.commit()

cursor.execute("SELECT * FROM cpu_usage")
print(cursor.fetchall())

conn.close()