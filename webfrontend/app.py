from flask import Flask
import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.datetime.now()
    return f"Hello, Flask 123 !, now={now}"