import os
from flask import Blueprint
import datetime as dt
import lib
cache_test_blue_print = Blueprint(name="cache_test", import_name=__name__)

@cache_test_blue_print.route("/cached_view")
@lib.FLASK_CACHE.cached(timeout=30)
def cache_test():
    now=dt.datetime.now()
    expiry = now+ dt.timedelta(seconds=30)
    return f"Hello world cache test . <br/> Now={dt.datetime.now()} <br/>Expiry={expiry}"

