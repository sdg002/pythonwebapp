import os
from flask import Blueprint
import datetime

version_blue_print = Blueprint(name="version", import_name=__name__)

@version_blue_print.route("/version")
def version():
    current_directory=os.path.dirname(__file__)
    version_file = os.path.join(current_directory, "../application_version.txt")
    version_text=None
    with open(version_file,"r") as f:
        version_text=f.readline()
    return version_text

