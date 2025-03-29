import dash
from dash import html
import os

dash.register_page(__name__, path='/',title=f'Home ({os.environ.get("ENVIRONMENT")})')

layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
])