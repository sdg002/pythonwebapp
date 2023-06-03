from flask import Flask
import datetime
import re
from views.version import version_blue_print
from views.environment import environment_blue_print
from views.home import home_blue_print
from views.about import about_blue_print

import logging

app = Flask(__name__)
app.register_blueprint(version_blue_print)
app.register_blueprint(environment_blue_print)
app.register_blueprint(home_blue_print)
app.register_blueprint(about_blue_print)
#app.register_blueprint(plotly_demo_blue_print)
logging.basicConfig(level=logging.INFO)

#
#First dash page registration
#
from views.dashdemo1 import make_dash, make_layout, define_callbacks
dash_app = make_dash(app)
dash_app.layout = make_layout()
define_callbacks()
