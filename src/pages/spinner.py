import logging
import os
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

import time

dash.register_page(
    __name__, title=f'Spinner ({os.environ.get("ENVIRONMENT")})')


def layout():
    html_layout = html.Div([
        dbc.Button("Start Long Operation",
                   id="spinner-start-button", n_clicks=0),
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
    Input("spinner-start-button", "n_clicks")
)
def update_output(n_clicks):
    logging.info(f"Inside update_output {n_clicks}")
    time.sleep(5)  # Simulate a delay
    if n_clicks > 0:
        time.sleep(5)  # Simulate a long operation
        return "Operation Complete!"
    return "Click the button to start the operation."
