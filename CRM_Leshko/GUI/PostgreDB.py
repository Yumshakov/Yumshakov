import psycopg

con = psycopg.connect(
  database="postgres",
  user="postgres",
  password="",
  host="127.0.0.1",
  port="5432"
)

print("Database opened successfully")