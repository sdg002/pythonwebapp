import os
import logging
import dash
from dash import html

dash.register_page(
    __name__, name='Another empty page', title=f'Archive ({os.environ.get("ENVIRONMENT")})', order=3)


def layout():
    logging.info(f'Page handler:{__name__}')
    elements = html.Div([
        html.H1('This is just another empty page'),
        html.Div('Demmo page content.'),
    ])
    return elements
