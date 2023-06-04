
import logging
from dash import Dash, html, callback, dcc, Input, Output
import plotly.express as px
import pandas as pd

logging.info("Begin-Fetching CSV data from REST API for CSV")
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')    
logging.info("End-Fetching CSV data from REST API for CSV")

def make_dash(server):
    logging.info("Inside make_dash")
    return Dash(
        server=server,
        url_base_pathname='/dash1/', title="Dash demo 1"
    )

def make_layout():
    logging.info("Inside make_layout")
    return html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')])

def define_callbacks():
    @callback(
        Output('graph-content', 'figure'),
        Input('dropdown-selection', 'value')
    )
    def update_graph(value):
        logging.info(f"Inside method update_graph, value={value}")
        dff = df[df.country==value]
        return px.line(dff, x='year', y='pop')


#
#https://hackersandslackers.com/plotly-dash-with-flask/
#
#Dash in a sub-folder and dashapp1/layout called from __init__.py
#https://github.com/okomarov/dash_on_flask/blob/master/app/dashapp1/layout.py
#
#
#https://github.com/tzelleke/flask-dash-app/blob/master/app/dash/demo.py
#The function init_dash in dash/dash.py and called from app/main.py
#
#https://www.geeksforgeeks.org/create-a-bar-chart-from-a-dataframe-with-plotly-and-flask/
#Nice example of using a template which has the JSON passed from the controller method and then JavaScript takes over
#
#
#https://plotly.com/dash/
#What is Dash? No JS required when you use Dash
#
#https://stackoverflow.com/questions/74762322/integrating-dash-and-flask-by-inserting-dash-chart-into-div-block-of-flask-templ
#IFRAME approach
#
# Rename to Dash demo