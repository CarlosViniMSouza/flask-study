from flask import Flask
# from app import routes

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1> Hello Flask! </h1>"
