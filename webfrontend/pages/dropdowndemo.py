import dash
from dash import html,dcc
import logging

dash.register_page(__name__)

#
# 1)Respond to the change in a call back
# 2)Populate the list of countries in a lazy loaded fashion
#

@dash.callback(
    dash.Output('country-output', 'children'),
    dash.Input('id-dropdown-country', 'value'))
def update_display(country: str):
    logging.info(f"Inside update_dislay {country}")
    return country

countres=["USA","UK", "Canada" ,"France"]
layout = html.Div([
    html.H1('This is a page with Drop down'),
    html.Div('Select a country.'),
    dcc.Dropdown(countres, 'Canada', id='id-dropdown-country'),
    html.Div(id='country-output'),
])