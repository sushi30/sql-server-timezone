import psycopg2
from datetime import datetime, timedelta
import pytz

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="test",
    password="test",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS test_dates (
        id SERIAL PRIMARY KEY,
        date_column DATE
    );
""")

# Insert rows for today
today = datetime.now(pytz.utc).date()
for _ in range(10):
    cur.execute("INSERT INTO test_dates (date_column) VALUES (%s)", (today,))

# Insert 1 row for yesterday
yesterday = today - timedelta(days=1)
cur.execute("INSERT INTO test_dates (date_column) VALUES (%s)", (yesterday,))

# Commit and close the connection
conn.commit()
cur.close()
conn.close()

print("Data inserted successfully.")