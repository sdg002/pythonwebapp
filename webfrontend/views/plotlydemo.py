import os
from flask import Blueprint, render_template
import datetime

plotly_demo_blue_print = Blueprint(name="plotly_demo", import_name=__name__)

@plotly_demo_blue_print.route("/plotlydemo")
def version():
    return render_template("plotlydemo.html")



