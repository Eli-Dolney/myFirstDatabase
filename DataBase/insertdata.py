import psycopg2

DB_NAME = "xkqcdldl"
DB_USER = "xkqcdldl"
DB_PASS = "IO6jwPB6G43IqgQSgL0DGVx6pCsrV4zB"
DB_HOST = "chunee.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

print("Database successfully connected")

cur = conn.cursor()
cur.execute("""

CREATE TABLE CONTACTS
(
NUMBER INT PRIMARY KEY,
NAME TEXT NOT NULL,
COMPANY TEXT NOT NULL,
EMAIL TEXT NOT NULL

)


""")

conn.commit()
print("Table created successfully")