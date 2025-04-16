import logging
import time
import os
import dash
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

dash.register_page(
    __name__, title=f'Spinner ({os.environ.get("ENVIRONMENT")})')

SLEEP_TIME_SECONDS = 5


def layout() -> object:
    elements = html.Div(children=[
        html.H1(
            id="banner", children=f'Loading Example {SLEEP_TIME_SECONDS} seconds. Please wait...'),

        dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading-output-1")
        ),

        dcc.Interval(
            id='interval-component',
            interval=1*100,  # in milliseconds
            n_intervals=0,
            max_intervals=0
        )
    ])
    return elements

# Define the callback to update the chart


# Define the callback to update the chart
@dash.callback(
    [Output('loading-output-1', 'children'), Output('banner', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    # Simulate a long computation
    logging.info(f"Interval triggered: {n}")
    time.sleep(SLEEP_TIME_SECONDS)

    # Create the chart
    figure = {
        'data': [
            go.Scatter(
                x=[1, 2, 3, 4, 5],
                y=[10, 11, 12, 13, 14],
                mode='lines+markers',
                name='Line 1'
            )
        ],
        'layout': {
            'title': 'Dash Plotly Line Chart with Loading Spinner'
        }
    }

    updated_banner = f'Loading complete after {SLEEP_TIME_SECONDS} seconds. '
    return dcc.Graph(
        id='example-graph',
        figure=figure), updated_banner
