from flask import Flask

# Create new web application with the name of the file
app = Flask(__name__)

# Specify route where this function will be executed.
# decorator
@app.route("/")
def index():
    return "Hello, world!"
