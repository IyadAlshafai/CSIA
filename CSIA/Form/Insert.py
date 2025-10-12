import pymysql.cursors
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Form.html')


@app.route('/insert', methods=['POST'])
def insert_feedback():
    feedback = request.form['feedback']
    overall = request.form['overall']
    experience = request.form['experience']
    response = request.form['response']

    try:
        cnx = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='Feedback_Database',
            port=8889
        )

        with cnx.cursor() as cursor:
            sql = """INSERT INTO Feedback (`Feedback_text`, `Overall_Rating (1 - 10)`, `Call_Experience (1 - 10)`, `Response_Time (1 - 10)`) VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (feedback, overall, experience, response))
        cnx.commit()
        return "Data inserted successfully!"

    except pymysql.Error as e:
        return f"Database error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
