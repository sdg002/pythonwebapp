import logging
import os
import flask as flask
import datetime
import plotly.express as px
import plotly
import pandas as pd
import json
import lib as lib
import numpy as np
import plotly.graph_objects as go

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
        return render_country_population(df=df_gapminder, country=None)
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

def render_country_population(df: pd.DataFrame,country: str)->str:
    logging.info(f"Inside function render_plotly_graph, selected country={country}, df={df}")

    df_countries = df["country"].unique()
    logging.info(f"Unique list of countries is: {len(df_countries)}")
    if country is None:
        country=df_countries[0]
        logging.info(f"No country was specified, therefore going to use '{country}'")

    dff = df[df['country']==country]
    title = f"Selected country is <b>{country}</b>"
    x_values = dff['year'].tolist()
    y_values = dff['pop'].tolist()

    fig = go.Figure(go.Scatter(x=x_values, y=y_values, mode='lines', name='Line Chart' ))
    fig.update_layout(title=title)
    graphJSON = json.dumps(fig, cls=  plotly.utils.PlotlyJSONEncoder)

    countries = list(df_countries)
    html_helper = lib.SelectElementHelper(values=countries, labels=countries, selected_value=country)
    return flask.render_template('plotlyadvanced.html', graphJSON=graphJSON, helper=html_helper)


@plotly_advanced_blue_print.route("/plotlyadvanced", methods=["POST"])
def plotly_demo_submit_country():
    try:
        logging.info(f"Post back")
        selected_country=flask.request.form["countrydropdown"]
        df_gapminder = get_data()
        return render_country_population(df=df_gapminder, country=selected_country)
    except Exception as err:
        logging.error(str(err))
        return str(err)

@plotly_advanced_blue_print.route("/plotlyadvancedhoverbothaxis")
def plotlyadvancedhoverbothaxis():
    #
    #https://plotly.com/python/hover-text-and-formatting/
    #Search for "Spike lines"
    #
    try:
        df = px.data.gapminder().query("continent=='Oceania'")
        fig = go.Figure()
        unique_countries=df["country"].unique()
        for country in unique_countries:
            dff = df[df["country"] == country]
            fig.add_trace(go.Scatter(
                x=dff["year"].tolist(),
                y=dff["lifeExp"].tolist(),
                mode="lines",
                name=country
            ))
        fig.update_layout(title="Population over Years for All Countries")
        fig.update_xaxes(showspikes=True)
        fig.update_yaxes(showspikes=True)
        fig.update_traces(mode="markers+lines")
        graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return flask.render_template('plotly_generic.html', graphJSON=graph_json, title="Population over Years for All Countries")
    except Exception as err:
        logging.error(str(err))
        return str(err)

#
#Selecting a hovermode in a figure created with plotly.graph_objects
#
@plotly_advanced_blue_print.route("/plotlyadvancedxaxis")
def plotlyadvancedhover_on_x_axis():
    #
    # https://plotly.com/python/hover-text-and-formatting/
    # Search for 'Selecting a hovermode in a figure created with plotly.graph_objects'
    #
    try:
        t = np.linspace(0, 2 * np.pi, 100)
        x_values = t.astype(float).tolist()
        y_sin = np.sin(t).astype(float).tolist()
        y_cos = np.cos(t).astype(float).tolist()
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_sin,
            name='sin(t)',
            mode='lines+markers',
            marker=dict(size=6, color='royalblue'),
            line=dict(color='royalblue')
        ))
        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_cos,
            name='cos(t)',
            mode='lines+markers',
            marker=dict(size=6, color='firebrick'),
            line=dict(color='firebrick')
        ))
        fig.update_layout(
            title="Sine and Cosine Functions with X-Axis Hover",
            xaxis_title="t (radians)",
            yaxis_title="Function value",
            hovermode='x unified',
            legend_title="Function",
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True)
        )
        graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return flask.render_template(
            'plotly_generic.html',
            graphJSON=graph_json,
            title="Hover lines along X axis only"
        )
    except Exception as err:
        logging.error(str(err))
        return "Error rendering scatter plot: " + str(err)

@plotly_advanced_blue_print.route("/plotlyadvancedhovertemplate")
def plotlyadvanced_hover_template():
    #
    #https://plotly.com/python/hover-text-and-formatting/
    # Search for 'Customizing hover text with a hovertemplate'
    #
    try:
        x = [1,2,3,4,5]
        y = [2.02825,1.63728,6.83839,4.8485,4.73463]
        custom_text = [f'My Custom text {i+1}' for i in range(len(x))]
        fig = go.Figure(go.Scatter(
            x = x,
            y = y,
            hovertemplate =
            '<i>Price</i>: $%{y:.2f}'+
            '<br><b>X</b>: %{x}<br>'+
            '<b>%{text}</b>',
            text = custom_text,
            showlegend = False))

        #did not work
        second_hover_template="<div class='second_hover_template'>Price</div>: %{y:$.2f}<extra></extra>"

        #this too did not work, just try bold
        #<b> works, but <div> and <strong> did not work!!!
        second_hover_template="<b>Price</b>: %{y:$.2f}<extra>Extra stuff</extra>"

        # Only a subset of HTML is supported https://community.plotly.com/t/can-you-add-html-to-plot-hovertext/306

        fig.add_trace(go.Scatter(
            x = [1,2,3,4,5],
            y = [3.02825,2.63728,4.83839,3.8485,1.73463],
            hovertemplate = second_hover_template,
            showlegend = False))

        fig.update_layout(
            hoverlabel_align = 'right',
            title = "Set hover text with hovertemplate")

        graphJSON = json.dumps(fig, cls=  plotly.utils.PlotlyJSONEncoder)
        return flask.render_template('plotly_generic.html', graphJSON=graphJSON, title="Hover lines along X axes only") 
    except Exception as err:
        logging.error(str(err))
        return str(err)
