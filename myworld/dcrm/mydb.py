import psycopg2

import environ
env = environ.Env()
environ.Env.read_env()

#establishing the connection
conn = psycopg2.connect(
   database=env("DB_NAME"), user=env("DB_USER"), password=env("DB_PASSWORD"), host=env("DB_HOST"), port= env("DB_PORT")
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''CREATE database mydb''';

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()