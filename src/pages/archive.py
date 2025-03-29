import dash
from dash import html
import os

dash.register_page(__name__,title=f'Archive ({os.environ.get("ENVIRONMENT")})')

layout = html.Div([
    html.H1('This is our Archive page'),
    html.Div('This is our Archive page content.'),
])