from flask import Flask
import datetime
import re
from views.version import version_blue_print
from views.environment import environment_blue_print
from views.home import home_blue_print

app = Flask(__name__)
app.register_blueprint(version_blue_print)
app.register_blueprint(environment_blue_print)
app.register_blueprint(home_blue_print)
