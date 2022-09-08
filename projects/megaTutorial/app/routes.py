from app import app

@app.route("/")
@app.route("/index")
def root():
    return "Hello Flask!"