from flask import Flask
import datetime
import re
from views.version import version_blue_print
from views.environment import environment_blue_print
from views.home import home_blue_print
from views.about import about_blue_print
from views.plotlydemo import plotly_blue_print
from views.formpostback import form_post_back
from views.plotlyadvanced import plotly_advanced_blue_print
import logging

app = Flask(__name__, static_folder='static',static_url_path='/static/')
app.register_blueprint(version_blue_print)
app.register_blueprint(environment_blue_print)
app.register_blueprint(home_blue_print)
app.register_blueprint(about_blue_print)
app.register_blueprint(plotly_blue_print)
app.register_blueprint(form_post_back)
app.register_blueprint(plotly_advanced_blue_print)

logging.basicConfig(level=logging.INFO)

#
#First dash page registration
#
from views.dashdemo1 import make_dash, make_layout, define_callbacks
dash_app = make_dash(app)
dash_app.layout = make_layout()
define_callbacks()
