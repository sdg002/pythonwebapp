import os
import flask as flask
import datetime
import plotly.express as px
import plotly.graph_objects as go
import plotly
import pandas as pd
import json

plotly_subplot_blue_print = flask.Blueprint(name="plotlysubplotsdemo", import_name=__name__)

@plotly_subplot_blue_print.route("/plotlysubplots")
def plotly_demo():
    df = px.data.iris()

    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", facet_col="species",
                    title="Adding Traces To Subplots Witin A Plotly Express Figure")

    reference_line = go.Scatter(x=[2, 4],
                                y=[4, 8],
                                mode="lines",
                                line=go.scatter.Line(color="gray"),
                                showlegend=False)

    fig.add_trace(reference_line, row=1, col=1)
    fig.add_trace(reference_line, row=1, col=2)
    fig.add_trace(reference_line, row=1, col=3)

    # Create graphJSON
    graphJSON = json.dumps(fig, cls=  plotly.utils.PlotlyJSONEncoder)
     
    # Use render_template to pass graphJSON to html
    return flask.render_template('plotlysubplotts.html', graphJSON=graphJSON)    

