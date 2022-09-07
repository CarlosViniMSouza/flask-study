from projects.megaTutorial.app import app
from dotenv import load_dotenv
import os


load_dotenv()
name = os.getenv("FLASK_NAME")
env = os.getenv("FLASK_ENV")

if __name__ == "__main__":
    # consult file in "note/optionalParam.txt"
    app.run(host="0.0.0.0", port=5555, debug=True)
