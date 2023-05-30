import os
from flask import Blueprint, render_template
import datetime

home_blue_print = Blueprint(name="home", import_name=__name__)

@home_blue_print.route("/")
def home():
    return render_template("home.html")

@home_blue_print.route("/link2")
def link2():
    return render_template("link2.html")

@home_blue_print.route("/link3")
def link3():
    return render_template("link3.html")

