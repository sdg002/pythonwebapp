import os
from flask import Blueprint
import datetime

environment_blue_print = Blueprint(name="environment", import_name=__name__)

@environment_blue_print.route("/environment")
def version():
    return os.environ.get("ENVIRONMENT","NOT-SET")



