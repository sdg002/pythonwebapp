# import os
# from flask import Blueprint, render_template
# import datetime

# plotly_demo_blue_print = Blueprint(name="plotly_demo", import_name=__name__)

# @plotly_demo_blue_print.route("/plotlydemo")
# def version():
#     return render_template("plotlydemo.html")



from dash import Dash, html, callback, dcc, Input, Output


def make_dash(server):
    return Dash(
        server=server,
        url_base_pathname='/dash1/', title="Dash demo 1"
    )

def make_layout():
    return html.Div(                                                                                                                                                                                                 
        [   
            html.A("Home",href='/', title="Click to go back to Home"),
            html.Hr(),                                                                                                                                                                                 
            html.P("Hey this is a demo Dash app 1. Type something in the text box:)"),                                                                                                                                                                     
            dcc.Input(id="input1"),                                                                                                                                                                                   
            html.Div(id="output1"),                                                                                                                                                                                   
        ]                                                                                                                                                                                                            
    )

def define_callbacks():
    @callback(
        Output("output1", "children"),
        Input("input1", "value"),
    )
    def show_output(text):
        return f"you entered: '{text}'"
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