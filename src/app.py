"""
Flask enty point
"""
import logging
import os
from flask import Flask
from flask import g
from flask_caching import Cache
from lib import DashHelper
from views.version import version_blue_print
from views.environment import environment_blue_print
from views.home import home_blue_print
from views.about import about_blue_print
from views.plotlydemo import plotly_blue_print
from views.formpostback import form_post_back
from views.plotlyadvanced import plotly_advanced_blue_print
from views.plotlydemosubplots import plotly_subplot_blue_print


def create_flask_app() -> Flask:
    app = Flask(__name__, static_folder='static', static_url_path='/static/')
    return app


def register_blue_prints(flask_app: Flask):
    from views.cache_test import cache_test_blue_print
    flask_app.register_blueprint(version_blue_print)
    flask_app.register_blueprint(environment_blue_print)
    flask_app.register_blueprint(home_blue_print)
    flask_app.register_blueprint(about_blue_print)
    flask_app.register_blueprint(plotly_blue_print)
    flask_app.register_blueprint(form_post_back)
    flask_app.register_blueprint(plotly_advanced_blue_print)
    flask_app.register_blueprint(plotly_subplot_blue_print)
    flask_app.register_blueprint(cache_test_blue_print)


def init_cache(flask_app: Flask) -> Cache:
    flask_app.config["DEBUG"] = True
    flask_app.config["CACHE_TYPE"] = "SimpleCache"
    flask_app.config['CACHE_DEFAULT_TIMEOUT'] = 300
    in_memory_cache = Cache(app=app)
    logging.info("Configuring of cache complete")
    return in_memory_cache


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

app = create_flask_app()
cache = init_cache(flask_app=app)


@app.before_request
def before_app_request():
    g.cache = cache


@app.context_processor
def inject_common_values():
    return {
        'environment': os.environ.get('ENVIRONMENT', None)
        # Add more key-value pairs as needed
    }


with app.app_context():
    g.cur_app = app
    g.cache = cache
    logging.info("Inside app_context")
    register_blue_prints(flask_app=app)
    DashHelper.register_dash_using_nav_bar(flask_app=app)
