import os
import flask as flask
import datetime
import plotly.express as px
import plotly
import pandas as pd
import json

plotly_advanced_blue_print = flask.Blueprint(name="plotlyadvanced", import_name=__name__)

@plotly_advanced_blue_print.route("/plotlyadvanced")
def plotly_demo():
    # Students data available in a list of list
    students = [['Akash', 34, 'Sydney', 'Australia'],
                ['Rithika', 30, 'Coimbatore', 'India'],
                ['Priya', 31, 'Coimbatore', 'India'],
                ['Sandy', 32, 'Tokyo', 'Japan'],
                ['Praneeth', 16, 'New York', 'US'],
                ['Praveen', 17, 'Toronto', 'Canada']]
     
    # Convert list to dataframe and assign column values
    df = pd.DataFrame(students,
                      columns=['Name', 'Age', 'City', 'Country'],
                      index=['a', 'b', 'c', 'd', 'e', 'f'])
     
    # Create Bar chart
    fig = px.bar(df, x='Name', y='Age', color='City', barmode='group')
     
    # Create graphJSON
    graphJSON = json.dumps(fig, cls=  plotly.utils.PlotlyJSONEncoder)
     
    # Use render_template to pass graphJSON to html
    return flask.render_template('plotlyadvanced.html', graphJSON=graphJSON)    

