from flask import Flask, render_template, request

app = Flask(__name__)

VALID_USERNAME = "s@gmail.com"
VALID_PASSWORD = "123456789"


@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["email"]
        password = request.form["password"]

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return render_template("Website.html", error=error)
        else:
            error = "Invalid username or password."

    return render_template("LoginPageFront.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)

