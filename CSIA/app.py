import pymysql

# Connecting to the database
cnx = ""
try:
  cnx = pymysql.connect (
    host='localhost',
    user='root',
    password='root',
    database='Feedback_Database',
    port=8889,
  )
except pymysql.Error as Er:
  print(Er)

cursor = cnx.cursor()
# Collecting the information form the database
cursor.execute('SELECT * FROM `Feedback`')

results = cursor.fetchall()

columns = [desc[0] for desc in cursor.description]
# Printing the results
for row in results:
    for col, val in zip(columns, row):
        print(f"{col}: {val}")
    print("-" * 40)

cnx.close()