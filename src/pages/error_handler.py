import dash
from dash import html, dcc
import logging
import os

dash.register_page(
    __name__, title=f'Error handler demo ({os.environ.get("ENVIRONMENT")})', order=50)


def layout():
    logging.info('CentrallPage handler:{__name__}')
    html_elements = html.Div([
        html.H1('Error handler demo'),
        html.Div('This is page content.. to be done.'),
    ])
    return html_elements
