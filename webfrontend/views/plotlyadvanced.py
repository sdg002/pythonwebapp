import logging
import os
import flask as flask
import datetime
import plotly.express as px
import plotly
import pandas as pd
import json

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
        #return plotly_demo()
        x=1/0
        pass
    except Exception as err:
        logging.error(str(err))
        return str(err)
        pass

def plotly_demo():
    host_url = flask.request.host_url
    ###
    host_url='https://app-saupythonflask001-dev.azurewebsites.net/'
    ###
    logging.info(f"Host url is {host_url}")
    data_file_url = f"{host_url}/static/data/gapminder.csv"
    logging.info(f"Going to download {data_file_url}")
    df_gapminder = pd.read_csv(data_file_url)
    logging.info(f"Found {len(df_gapminder)} records in the dataframe ")
    df_countries = df_gapminder["country"].unique()
    logging.info(f"Unique list of countries is: {len(df_countries)}")


    #you  were looking at this 
    #SelectField
    # Students data available in a list of list
    students = [['Akash', 34, 'Sydney', 'Australia'],
                ['Rithika', 30, 'Coimbatore', 'India'],
                ['Priya', 31, 'Coimbatore', 'India'],
                ['Sandy', 32, 'Tokyo', 'Japan'],
                ['Praneeth', 16, 'New York', 'US'],
                ['Praveen', 17, 'Toronto', 'Canada']]
     
    # Convert list to dataframe and assign column values
    df_gapminder = pd.DataFrame(students,
                      columns=['Name', 'Age', 'City', 'Country'],
                      index=['a', 'b', 'c', 'd', 'e', 'f'])
     
    # Create Bar chart
    fig = px.bar(df_gapminder, x='Name', y='Age', color='City', barmode='group')
     
    # Create graphJSON
    graphJSON = json.dumps(fig, cls=  plotly.utils.PlotlyJSONEncoder)
     
    
    countries = list(df_countries)
    # you were here, you got the countries populated, now look at Dash and create a line chart (filter on the selected country, default selection is None)
    # extend HtmlHelper to render the selected item
    # when postback happens re-render the same view - one common parameteried function to render
    html_helper = HtmlHelper(values=countries, labels=countries)
    return flask.render_template('plotlyadvanced.html', graphJSON=graphJSON, helper=html_helper)


class HtmlHelper():
    """docstring for HtmlHelper Provides helper methods to simplify the generation of basic HTML elements """
    def __init__(self, labels:list, values:list):
        self.values= [] if values is None else values
        #TODO check for type
        self.labels=[] if labels is None else labels
        if len(self.values) != len(self.labels):
            raise ValueError("The lables and values of the SELECT items should have the same length")
        pass

    def select_element(self, class_name='', name='',id='',):
        html=''
        html+=f'<select class="{class_name}" name="{name}" id="{id}" >'
        for index in range(len(self.values)):            
            html+=f'<option value="{self.values[index]}">{self.labels[index]}</option>'
        html+='</select>'
        return html


@plotly_advanced_blue_print.route("/plotlyadvanced", methods=["POST"])
def plotly_demo_submit():
    return f"submit received {flask.request.form}"
