import os
from flask import Blueprint, render_template
import datetime

home_blue_print = Blueprint(name="home", import_name=__name__)

@home_blue_print.route("/")
def home():
    return render_template("home.html")

# @app.route("/")
# def home():
#     now = datetime.datetime.now()
#     return f"Hello, Flask 123 !, now={now}"