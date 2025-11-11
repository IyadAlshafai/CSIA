from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__, template_folder='templates')

VALID_USERNAME = "s@gmail.com"
VALID_PASSWORD = "123456789"


@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["email"]
        password = request.form["password"]

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            # Redirect to feedback dashboard after successful login
            return redirect(url_for("feedback_dashboard"))
        else:
            error = "Invalid username or password."
    return render_template("LoginPageFront.html", error=error)

@app.route("/website", methods=["GET"])
def feedback_dashboard():
    # Get filter values from URL
    year = request.args.get("year", type=int)
    month = request.args.get("month", type=int)

    try:
        # Connect to MySQL
        cnx = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="Feedback_Database",
            port=8889
        )

        with cnx.cursor() as cursor:
            if year and month:
                # Filtered query by year and month
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
                # Show all feedback if no filter is applied
                cursor.execute("SELECT Feedback_text FROM Feedback;")
                feedback_list = [row[0] for row in cursor.fetchall()]

                cursor.execute("SELECT AVG(Overall_Rating) FROM Feedback;")
                result = cursor.fetchone()
                overall = result[0] if result and result[0] else 0

        cnx.close()

        # Convert overall rating to percentage for chart display
        overallpercent = overall * 10
        overallp = f"{overallpercent:.0f}%"

        return render_template(
            "Website.html",
            overall=overall,
            comment=feedback_list,
            percent=overallp
        )

    except pymysql.Error as e:
        return f"Database error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
