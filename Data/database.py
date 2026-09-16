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

    cursor.execute("SELECT * FROM cpu_usage")
    print(f"[{timestamp}]", cursor.fetchall())

    conn.close()

if __name__ == "__main__":
    init_db()
    store_cpu_data()
    schedule.every(5).seconds.do(store_cpu_data)

    print("Scheduler running. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)   