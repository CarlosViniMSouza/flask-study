from app import app

@app.route("/")
@app.route("/index")
def root():
    user = {'username': 'Miguel'}
    return """
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, """ + user['username'] + """!</h1>
            </body>
        </html>
    """