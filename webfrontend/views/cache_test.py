import os
from flask import Blueprint
import datetime

cache_test_blue_print = Blueprint(name="cache_test", import_name=__name__)

@cache_test_blue_print.route("/cached_view")
def version():
    return f"Hello world cache test"

