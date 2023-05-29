from flask import Flask
import datetime
import re
from views.version import version_blue_print

app = Flask(__name__)
app.register_blueprint(version_blue_print)

@app.route("/")
def home():
    now = datetime.datetime.now()
    return f"Hello, Flask 123 !, now={now}"