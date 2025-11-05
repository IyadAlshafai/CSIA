from flask import Flask, render_template, request
import pymysql

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=["GET"])
def filter_data():
    year = request.args.get('year', type=int)
    month = request.args.get('month', type=int)

    try:
        cnx = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='Feedback_Database',
            port=8889
        )

        with cnx.cursor() as cursor:
            if year and month:
                # Filtered query
                cursor.execute("""
                    SELECT Feedback_text FROM Feedback
                    WHERE YEAR(created_at) = %s AND MONTH(created_at) = %s;
                """, (year, month))
                feedback_list = [row[0] for row in cursor.fetchall()]

                cursor.execute("""
                    SELECT AVG(Overall_Rating) FROM Feedback
                    WHERE YEAR(created_at) = %s AND MONTH(created_at) = %s;
                """, (year, month))
                result = cursor.fetchone()
                overall = result[0] if result and result[0] else 0
            else:
                # No filter → show all
                cursor.execute("SELECT Feedback_text FROM Feedback;")
                feedback_list = [row[0] for row in cursor.fetchall()]

                cursor.execute("SELECT AVG(Overall_Rating) FROM Feedback;")
                result = cursor.fetchone()
                overall = result[0] if result and result[0] else 0

        cnx.close()

        overallpercent = overall * 10
        overallp = f"{overallpercent}%"

        return render_template('Website.html',
                               overall=overall,
                               comment=feedback_list,
                               percent=overallp)

    except pymysql.Error as e:
        return f"Database error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
