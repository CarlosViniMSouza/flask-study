from flask import Flask, render_template
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


@app.route("/admin")
def hello_admin():
    return "Hello Admin"


@app.route("/guest/<guest>")
def hello_guest(guest):
    return f"Hello {guest} as Guest"


if __name__ == "__main__":
    # consult file in "note/optionalParam.txt"
    app.run(host="0.0.0.0", port=5555, debug=True)
