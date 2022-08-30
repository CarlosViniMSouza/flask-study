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
    app.run(host="0.0.0.0", port=5050, debug=True)


"""
Optional Parameters:

1. host = Hostname to listen on. Defaults to 127.0.0.1 (localhost). 
            Set to ‘0.0.0.0’ to have server available externally
2. port = Defaults to 5000
3. debug = Defaults to false. If set to true, provides a debug information
4. options = To be forwarded to underlying Werkzeug server.
"""

"""
Methods & Description:

1. GET -> Sends data in unencrypted form to the server. Most common method.
2. HEAD -> Same as GET, but without response body
3. POST -> Used to send HTML form data to server. Data received by POST method is not cached by server.
4. PUT -> Replaces all current representations of the target resource with the uploaded content.
5. DELETE -> Removes all current representations of the target resource given by a URL
"""
