import os
import logging
import dash
from dash import html

dash.register_page(__name__, path='/plotlythemes',
                   title=f'Plotly Themes ({os.environ.get("ENVIRONMENT")})', order=8)


def layout():
    logging.info('Page handler:{__name__}')
    html_elements = html.Div([
        html.H1('This is our Plotly Themes page'),
        html.Div('This is our Plotly Themes page content.'),
        html.A('Go back to the landing page', href='/'),
    ])
    return html_elements
