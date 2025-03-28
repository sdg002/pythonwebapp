import logging
from flask import Blueprint
import flask
import datetime as dt
import lib
cache_test_blue_print = Blueprint(name="cache_test", import_name=__name__)

@cache_test_blue_print.route("/cached_view")
@lib.FLASK_CACHE.cached(timeout=30)
def cache_test():
    now=dt.datetime.now()
    expiry = now+ dt.timedelta(seconds=30)
    logging.info("Inside cache_test view")
    key_values={"current_time":now, "expiry_time":expiry}
    return flask.render_template("cache_test.html",**key_values)

