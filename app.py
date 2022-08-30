from flask import Flask, escape, url_for, redirect, request, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
name = os.getenv("FLASK_NAME")
env = os.getenv("FLASK_ENV")


# HTML file can be rendered by the render_template() function.
# OBS.: Flask will try to find the HTML file on "templates" folder
@app.route("/")
def root():
    return render_template("index.html")


@app.route("/calculate/<int:score>")
def calcTemp(score):
    # 'marks' is 'score' on HTML file rendering
    return render_template("calculate.html", marks=score)


@app.route("/admin")
def hello_admin():
    return "Hello Admin"


@app.route("/guest/<guest>")
def hello_guest(guest):
    return f"Hello {guest} as Guest"


# The url_for() function is very useful for dynamically building a URL for a specific function.
@app.route("/hello/<user>")
def hello_user(user):
    if user == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect((url_for("hello_guest", guest=user)))


@app.route("/blogs/<int:blogID>")
def blogs(blogID):
    return f"This blog have the ID: {escape(blogID)}"


@app.route("/research")
def research():
    return render_template("form/research.html")


@app.route("/resultResearch", methods=["GET", "POST"])
def resultResearch():
    if request.method == "POST":
        result = request.form
        return render_template("form/result.html", result=result)
    else:
        return redirect(url_for("hello_guest"))


if __name__ == "__main__":
    # consult file in "note/pptionalParam.txt"
    app.run(host="0.0.0.0", port=5050, debug=True)
