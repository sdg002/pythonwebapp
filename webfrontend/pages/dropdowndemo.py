import dash
from dash import html,dcc

dash.register_page(__name__)

countres=["USA","UK", "Canada" ,"France"]
layout = html.Div([
    html.H1('This is a page with Drop down'),
    html.Div('Select a country.'),
    dcc.Dropdown(countres, 'Canada', id='dropdown-selection'),
])