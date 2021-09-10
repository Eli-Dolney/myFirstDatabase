import psycopg2

DB_NAME = "xkqcdldl"
DB_USER = "xkqcdldl"
DB_PASS = "IO6jwPB6G43IqgQSgL0DGVx6pCsrV4zB"
DB_HOST = "chunee.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

print("Database successfully connected")

cur = conn.cursor()

cur.execute("SELECT NUMBER, NAME, COMPANY, EMAIL FROM contacts")

rows = cur.fetchall()

for data in rows:
    print("NUMBER : " + str(data[0]))
    print("NAME : " + data[1])
    print("COMPANY : " + data[2])
    print("EMAIL : " + data[3])

print("Data Selected Successfully")
conn.close()