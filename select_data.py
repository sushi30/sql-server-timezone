import psycopg2
from datetime import datetime
import pytz

# Function to change the timezone on the server
def set_server_timezone(timezone):
    conn = psycopg2.connect(
        dbname="postgres",
        user="test",
        password="test",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"ALTER SYSTEM SET timezone = '{timezone}'")
    cur.execute("SELECT pg_reload_conf()")
    cur.close()
    conn.close()

# Function to get count for the current date
def get_count_for_current_date():
    conn = psycopg2.connect(
        dbname="postgres",
        user="test",
        password="test",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM test_dates WHERE date_column = CURRENT_DATE")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return count

# Set server timezone to UTC and get count
set_server_timezone('UTC')
utc_count = get_count_for_current_date()
print(f"UTC Date Count for CURRENT_DATE: {utc_count}")

# Set server timezone to Eastern Time and get count
for i in range(24):
    set_server_timezone(f'-{i}')
    modified_timezone = get_count_for_current_date()
    if modified_timezone < 10:
        print(f"Count for CURRENT_DATE on timezone -{i}: {modified_timezone}")
        break