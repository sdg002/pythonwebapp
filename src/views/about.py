import os
from flask import Blueprint ,render_template
import datetime
import logging
import lib as lib

about_blue_print = Blueprint(name="about", import_name=__name__)

@about_blue_print.route("/about")
def version():
    current_environment = os.environ.get("ENVIRONMENT", None)
    current_version = lib.__version__
    logging.info(f"Environment is {current_environment}")
    logging.info(f"Application version is {current_version}")
    return render_template("about.html", version=current_version)
