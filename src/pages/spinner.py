import os
import dash
from dash import html


dash.register_page(
    __name__, title=f'Spinner ({os.environ.get("ENVIRONMENT")})')


def layout():
    html_layout = html.Div([
        html.H1('This demonstrates a spinner'),
        html.Div('This is our Spinner content.'),
    ])
    return html_layout
