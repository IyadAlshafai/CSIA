import pymysql.cursors
from flask import Flask, render_template, request

cnx = ""
try:
    cnx = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='Feedback_Database',
        port=8889,
    )
except pymysql.Error as Er:
    print(Er)

with cnx:
    with cnx.cursor() as cursor:
        sql = "INSERT INTO `Feedback` (`Feedback_text`, `Overall_Rating (1 - 10)`, `Call_Experience (1 - 10)`, `Response_Time (1 - 10)`) VALUES (%s, %s, %s, %s)"
    cnx.commit()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Form.html')


@app.route('/Insert.py', methods=['POST'])
def run_script():
    # Your Python code to execute
    result = "Python script executed successfully!"
    return result
