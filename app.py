from flask import Flask, escape

app = Flask(__name__)


# Testing URLs distincts

@app.route("/hello")
def hello_world():  # put application's code here
    return "Hello World!"


@app.route("/hello/<user>")
def hello_user(user):
    return f"Hello {escape(user)}"


@app.route("/blogs/<int:blogID>")
def blogs(blogID):
    return f"This blog have the ID: {escape(blogID)}"


"""
The add_url_rule() function of an application object is also available 
to bind a URL with a function as in the above example, route() is used.
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

"""
app.run(host, port, debug, options)

All parameters are optional:

1. host = Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally
2. port = Defaults to 5000
3. debug = Defaults to false. If set to true, provides a debug information
4. options = To be forwarded to underlying Werkzeug server.
"""
