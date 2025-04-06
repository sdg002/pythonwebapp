import dash
from dash import html
import os

dash.register_page(
    __name__, title=f'Spinner ({os.environ.get("ENVIRONMENT")})')

layout = html.Div([
    html.H1('Demonstrate spinner with chart'),
    html.Div('Show a chart after a long running operation.'),
])
