import os
import logging
import dash
from dash import html

dash.register_page(__name__, path='/',
                   title=f'Home ({os.environ.get("ENVIRONMENT")})', order=0)


def layout():
    logging.info('Page handler:{__name__}')
    html_elements = html.Div([
        html.H1('This is our Home page'),
        html.Div('This is our Home page content.'),
    ])
    return html_elements
