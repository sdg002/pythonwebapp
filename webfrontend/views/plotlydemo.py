import os
import flask as flask
import datetime

plotly_blue_print = flask.Blueprint(name="plotly", import_name=__name__)

@plotly_blue_print.route("/plotly")
def plotly_demo():
    return flask.render_template("plotly.html")

