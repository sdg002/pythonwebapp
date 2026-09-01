import time
import logging
import os
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

LONG_OPERATION_TIME = 5  # seconds

dash.register_page(
    __name__, name="Start long operation", title=f'Spinner ({os.environ.get("ENVIRONMENT")})', order=5)


def layout():
    html_layout = html.Div([
        html.P("Click on the button to start a long operation"),
        dbc.Button(f"Start Long Operation {LONG_OPERATION_TIME} seconds",
                   id="spinner-start-button", n_clicks=0),
        dcc.Loading(
            id="spinner-loading",
            type="circle",
            show_initially=False,
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
    logging.info(f"Inside update_output call back {n_clicks}")
    if n_clicks > 0:
        start_time = time.time()  # Record the start time
        time.sleep(LONG_OPERATION_TIME)  # Simulate a long operation
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        return html.Div([
            html.H4("Long operation completed!"),
            html.P(f"Operation took {elapsed_time:.2f} seconds.")
        ])
    return ""
