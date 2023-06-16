import logging
import os
import flask as flask
import datetime
import plotly.express as px
import plotly
import pandas as pd
import json
import lib as lib

GAP_MINDER_DATA_SOURCE='https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv'
plotly_advanced_blue_print = flask.Blueprint(name="plotlyadvanced", import_name=__name__)

@plotly_advanced_blue_print.route("/plotlyadvanced2", methods=["GET"])
def plotly_demo_temp():
    #you were here 
    #request.host_url=http://app-saupythonflask001-dev.azurewebsites.net/
    host_url = flask.request.host_url
    d = dict()
    d["name1"] = "value 1"
    d["request.host_url"] = flask.request.host_url
    d["request.host"] = flask.request.host
    d["request.full_path"] = flask.request.full_path
    d["request.date"] = flask.request.date
    d["request.cookies"] = str(flask.request.cookies)
    d["request.headers"] = str(flask.request.headers)
    display=""
    for item in d.keys():
        display=display + f"{item}={d[item]}<br/>"
    return display


@plotly_advanced_blue_print.route("/plotlyadvanced", methods=["GET"])
def plotly_demo_outer():
    try:
        return plotly_demo()
        pass
    except Exception as err:
        logging.error(str(err))
        return str(err)
        pass

def plotly_demo():
    host_url = flask.request.host_url
    ###
    #this does not work ,the web app times out. works fine locally
    #host_url='https://app-saupythonflask001-dev.azurewebsites.net/'
    ###
    logging.info(f"Host url is {host_url}")
    #data_file_url = f"{host_url}/static/data/gapminder.csv"
    data_file_url=GAP_MINDER_DATA_SOURCE
    logging.info(f"Going to download {data_file_url}")
    df_gapminder = pd.read_csv(data_file_url)
    logging.info(f"Found {len(df_gapminder)} records in the dataframe ")
    df_countries = df_gapminder["country"].unique()
    logging.info(f"Unique list of countries is: {len(df_countries)}")
     
    selected_country=df_countries[0]
    dff = df_gapminder[df_gapminder['country']==selected_country]
    title = f"Selected country is <b>{selected_country}</b>"
    fig=px.line(dff, x='year', y='pop', title=title)
    graphJSON = json.dumps(fig, cls=  plotly.utils.PlotlyJSONEncoder)
    
    countries = list(df_countries)
    # you were here, you got the countries populated, now look at Dash and create a line chart (filter on the selected country, default selection is None)
    # extend HtmlHelper to render the selected item
    # when postback happens re-render the same view - one common parameteried function to render
    html_helper = lib.SelectElementHelper(values=countries, labels=countries)
    return flask.render_template('plotlyadvanced.html', graphJSON=graphJSON, helper=html_helper)


@plotly_advanced_blue_print.route("/plotlyadvanced", methods=["POST"])
def plotly_demo_submit():
    return f"submit received {flask.request.form}"
