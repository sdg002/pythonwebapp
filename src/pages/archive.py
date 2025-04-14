import os
import logging
import dash
from dash import html

dash.register_page(
    __name__, title=f'Archive ({os.environ.get("ENVIRONMENT")})')


def layout():
<<<<<<< HEAD
    logging.info(f"Inside handler:{__name__}")
=======
    logging.info(f'Page handler:{__name__}')
>>>>>>> Changed archive/analytics to function (#51)
    elements = html.Div([
        html.H1('This is our Archive page'),
        html.Div('This is our Archive page content.'),
    ])
    return elements
