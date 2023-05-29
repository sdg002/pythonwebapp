from flask import Blueprint
import datetime

version_blue_print = Blueprint(name="version", import_name=__name__)

@version_blue_print.route("/version")
def version():
    return f"version is {datetime.datetime.utcnow()}"
