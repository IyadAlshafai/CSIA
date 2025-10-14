import pymysql.cursors
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


# Loads the form template
@app.route('/')
def index():
    return render_template('Form.html')


@app.route('/insert', methods=['POST'])
def insert_feedback():
    # Collect the feedback from the form
    feedback = request.form['comments']
    overall = request.form['rating']
    experience = request.form['call_experience']
    response = request.form['response_time']

    # Connecting to the database
    try:
        cnx = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='Feedback_Database',
            port=8889
        )
        # Generating the user ID for the feedback
        with cnx.cursor() as cursor:
            cursor.execute("SELECT user_ID FROM Feedback ORDER BY user_ID DESC LIMIT 1")
            row = cursor.fetchone()
            if row:
                new_user_id = row[0] + 1
            else:
                new_user_id = 1

            cursor.execute("INSERT INTO Users (User_ID) VALUES (%s)", (new_user_id,))
            # Inserting the information collected from the form
            sql = """INSERT INTO Feedback (user_ID, `Feedback_text`, `Overall_Rating`,
            `Call_Experience`, `Response_Time`) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (new_user_id, feedback, overall, experience, response))
        cnx.commit()
        cnx.close()
        return f"Feedback successfully submitted!"
    # Error if something goes wrong
    except pymysql.Error as e:
        return f"Database error: {e}"


# Essential for the app to run
if __name__ == "__main__":
    app.run(debug=True)
