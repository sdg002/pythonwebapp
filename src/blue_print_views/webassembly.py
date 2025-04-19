import flask as flask

web_assembly_blue_print = flask.Blueprint(
    name="webassembly", import_name=__name__)


@web_assembly_blue_print.route("/webassembly1")
def plotly_demo():
    # return flask.render_template('plotly.html', graphJSON=graphJSON)
    return 'Hello world!'
