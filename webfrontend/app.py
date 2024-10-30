"""
Flask enty point
"""
import logging
from flask import Flask
from views.version import version_blue_print
from views.environment import environment_blue_print
from views.home import home_blue_print
from views.about import about_blue_print
from views.plotlydemo import plotly_blue_print
from views.formpostback import form_post_back
from views.plotlyadvanced import plotly_advanced_blue_print
from views.plotlydemosubplots import plotly_subplot_blue_print
from views.cache_test import cache_test_blue_print
import lib as lib


def create_flask_app()->Flask:
    app = Flask(__name__, static_folder='static',static_url_path='/static/')
    app.register_blueprint(version_blue_print)
    app.register_blueprint(environment_blue_print)
    app.register_blueprint(home_blue_print)
    app.register_blueprint(about_blue_print)
    app.register_blueprint(plotly_blue_print)
    app.register_blueprint(form_post_back)
    app.register_blueprint(plotly_advanced_blue_print)
    app.register_blueprint(plotly_subplot_blue_print)
    app.register_blueprint(cache_test_blue_print)
    lib.FLASK_APP = app
    return app

def init_cache(flask_app:Flask):
    flask_app.config["DEBUG"]=True
    flask_app.config["CACHE_TYPE"]="SimpleCache"
    logging.info("Configuring of cache complete")

def register_dash():
    import dash
    from dash import Dash, html, dcc
    from flask import g
    logging.info("Inside register_dash")
    dash_app = Dash(use_pages=True, server=g.cur_app,  url_base_pathname="/dash/")

    nav_bar=[]
    for page in dash.page_registry.values():
        nav_bar.append(html.Span(" | "))
        logging.info(f"Found dash page {page['path']}")
        nav_bar.append(dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"]))

    nav_bar.append(html.Span(" | "))
    nav_bar.append(html.A("Back to home page", href="/"))


    dash_app.layout = html.Div([
        html.H1('Multi-page app with Dash Pages'),
        html.Div(nav_bar),
        html.Hr(),
        dash.page_container
    ])
    logging.info("Register dash complete")

        # html.Div([
        #     html.Div(
        #         dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        #     ) for page in dash.page_registry.values()
        # ]),

logging.basicConfig(level=logging.INFO)
app = create_flask_app()
init_cache(flask_app=app)

with app.app_context():
    from flask import g
    g.cur_app = app
    logging.info("Inside app_context")
    register_dash()

