import sqlite3
import schedule
import time
from datetime import datetime
from Core.cpu import get_cpu

DB_PATH = 'data.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cpu_usage (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usage REAL,
        frequency REAL,
        physical_cores INTEGER,
        logical_cores INTEGER,
        created_at TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def store_cpu_data():
    CPU = get_cpu()

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO cpu_usage (usage, frequency, physical_cores, logical_cores, created_at) VALUES (:usage, :frequency, :physical_cores, :logical_cores, :created_at)",
        {**CPU, "created_at": timestamp}
    )
    conn.commit()

    cursor.execute("SELECT * FROM cpu_usage ORDER BY created_at DESC LIMIT 1")
    print(f"[{timestamp}]", cursor.fetchall())

    conn.close()

def get_cpu_usage(start=None, end=None, limit=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT * FROM cpu_usage WHERE 1=1"
    params = []

    if start:
        query += " AND created_at >= ?"
        params.append(start)
    if end:
        query += " AND created_at <= ?"
        params.append(end)

    query += " ORDER BY created_at DESC"
    if limit:
        query += " LIMIT ?"
        params.append(limit)

    cursor.execute(query, params)
    usage = cursor.fetchall()

    conn.close()
    return usage   

if __name__ == "__main__":
    init_db()
    store_cpu_data()

    observations = get_cpu_usage(limit=5)

    for observation in observations:
        print(observation)

    schedule.every(5).seconds.do(store_cpu_data)

    print("Scheduler running. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)