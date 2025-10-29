from flask import Flask, render_template, request

app = Flask(__name__)
# this is the information that needs to be entered to access the feedback
VALID_USERNAME = "s@gmail.com"
VALID_PASSWORD = "123456789"


@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        # Collecting the information from what is inserted
        username = request.form["email"]
        password = request.form["password"]
        # Comparing it to the valid information given
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return render_template("Website.html", error=error)
        else:
            # Doesn't let the user through unless they get it correct
            error = "Invalid username or password."
    # Sends them back to the first page
    return render_template("LoginPageFront.html", error=error)


# this is essential for the app to run
if __name__ == "__main__":
    app.run(debug=True)

