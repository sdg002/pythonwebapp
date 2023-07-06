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
        df_gapminder = get_data()
        return render_plotly_graph(df=df_gapminder, country=None)
    except Exception as err:
        logging.info(str(err))
        logging.error(str(err))
        return str(err)


def get_data()->pd.DataFrame:
    ###
    #this does not work on Azure ,the web app times out. works fine locally
    #host_url = flask.request.host_url
    #host_url='https://app-saupythonflask001-dev.azurewebsites.net/' #this does not work either
    #logging.info(f"Host url is {host_url}")
    #data_file_url = f"{host_url}/static/data/gapminder.csv"
    ###
        
    data_file_url=GAP_MINDER_DATA_SOURCE
    logging.info(f"Going to download {data_file_url}")
    df_gapminder = pd.read_csv(data_file_url)
    logging.info(f"Found {len(df_gapminder)} records in the dataframe ")
    return df_gapminder

def render_plotly_graph(df: pd.DataFrame,country: str)->str:
    logging.info(f"Inside function render_plotly_graph, selected country={country}, df={df}")

    df_countries = df["country"].unique()
    logging.info(f"Unique list of countries is: {len(df_countries)}")
    if country is None:
        country=df_countries[0]
        logging.info(f"No country was specified, therefore going to use '{country}'")

    dff = df[df['country']==country]
    title = f"Selected country is <b>{country}</b>"
    fig=px.line(dff, x='year', y='pop', title=title)
    graphJSON = json.dumps(fig, cls=  plotly.utils.PlotlyJSONEncoder)
    
    countries = list(df_countries)
    # extend HtmlHelper to render the selected item
    html_helper = lib.SelectElementHelper(values=countries, labels=countries, selected_value=country)
    return flask.render_template('plotlyadvanced.html', graphJSON=graphJSON, helper=html_helper)


@plotly_advanced_blue_print.route("/plotlyadvanced", methods=["POST"])
def plotly_demo_submit():
    try:
        logging.info(f"Post back")
        selected_country=flask.request.form["countrydropdown"]
        df_gapminder = get_data()
        return render_plotly_graph(df=df_gapminder, country=selected_country)
    except Exception as err:
        logging.error(str(err))
        return str(err)

@plotly_advanced_blue_print.route("/plotlyadvancedhoverbothaxis")
def plotlyadvancedhoverbothaxis():
    #
    #https://plotly.com/python/hover-text-and-formatting/
    #
    try:
        df = px.data.gapminder().query("continent=='Oceania'")

        fig = px.line(df, x="year", y="lifeExp", color="country", title="Spike lines")
        fig.update_traces(mode="markers+lines")

        fig.update_xaxes(showspikes=True)
        fig.update_yaxes(showspikes=True)        
        graphJSON = json.dumps(fig, cls=  plotly.utils.PlotlyJSONEncoder)
        return flask.render_template('plotly_generic.html', graphJSON=graphJSON, title="Hover lines along X and Y axes") 
    except Exception as err:
        logging.error(str(err))
        return str(err)
