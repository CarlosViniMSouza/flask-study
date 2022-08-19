from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

"""
app.run(host, port, debug, options)

All parameters are optional:

1. host = Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally
2. port = Defaults to 5000
3. debug = Defaults to false. If set to true, provides a debug information
4. options = To be forwarded to underlying Werkzeug server.
"""