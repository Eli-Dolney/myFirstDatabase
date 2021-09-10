import psycopg2

DB_NAME = "xkqcdldl"
DB_USER = "xkqcdldl"
DB_PASS = "IO6jwPB6G43IqgQSgL0DGVx6pCsrV4zB"
DB_HOST = "chunee.db.elephantsql.com"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)

    print("Database connected successfully")

except:
    print("Database not connected")