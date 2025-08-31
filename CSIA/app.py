from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/Feedback_Database'
config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'port': 8889,
  'database': 'feedback_database',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor(dictionary=True)

cursor.execute('SELECT `User_id`, `name` FROM `Users`')
results = cursor.fetchall()

for row in results:
  id = row['User_id']
  title = row['name']
  print('%s | %s' % (id, title))


db = SQLAlchemy(app)
