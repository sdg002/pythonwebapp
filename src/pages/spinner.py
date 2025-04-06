import os
import dash
from dash import html, dcc, Input, Output
import time

dash.register_page(
    __name__, title=f'Spinner ({os.environ.get("ENVIRONMENT")})')


def layout():
    html_layout = html.Div([
        dcc.Input(id='spinner-input', value='initial value'),
        dcc.Loading(
            id="spinner-loading",
            type="default",
            children=html.Div(id="spinner-loading-output")
        )
    ])
    return html_layout


# Callback to simulate a long-running operation


@dash.callback(
    Output("spinner-loading-output", "children"),
    Input("spinner-input", "value")
)
def update_output(value):
    time.sleep(5)  # Simulate a delay
    return f'Output: {value}'
