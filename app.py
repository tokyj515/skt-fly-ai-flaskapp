from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, WepApp!"


@app.route("/hello")
def hello():
    return "Hello, YUjin!!"
