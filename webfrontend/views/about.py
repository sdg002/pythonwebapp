import os
from flask import Blueprint ,render_template
import datetime

about_blue_print = Blueprint(name="about", import_name=__name__)

@about_blue_print.route("/about")
def version():
    return render_template("about.html")
