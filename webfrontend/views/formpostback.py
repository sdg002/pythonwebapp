import os
from flask import Blueprint, render_template
import datetime

form_post_back = Blueprint(name="form_post_back", import_name=__name__)

@form_post_back.route("/formpostback")
def home():
    return render_template("formpostback.html")


