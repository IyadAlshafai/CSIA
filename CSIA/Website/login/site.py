from flask import Flask, render_template
import pymysql

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    try:
        cnx = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='Feedback_Database',
            port=8889
        )

        with cnx.cursor() as cursor:
            cursor.execute("SELECT AVG(Overall_Rating) FROM Feedback;")
            result = cursor.fetchone()
            if result and result[0] is not None:
                overall_avg = round(result[0], 2)
            else:
                overall_avg = 0  # default value
            print(overall_avg)
            print(type(overall_avg))
        cnx.close()

    except pymysql.Error as e:
        return f"Database error: {e}"

    return render_template('Website.html', overall=float(overall_avg or 0))


if __name__ == '__main__':
    app.run(debug=True)
