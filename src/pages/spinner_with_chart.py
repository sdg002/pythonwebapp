import logging
import time
import os
import random
import plotly.graph_objs as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

dash.register_page(
    __name__, name="Load chart after delay", title=f'Spinner ({os.environ.get("ENVIRONMENT")})', order=6)

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


def generate_numbers_with_variation(n, m, variation=2):
    """
    Generate a list of numbers from n to m with random variation added to each number.

    :param n: Starting number (inclusive)
    :param m: Ending number (inclusive)
    :param variation: Maximum random variation to add/subtract
    :return: List of numbers with random variation
    """
    return [x + random.uniform(-variation, variation) for x in range(n, m + 1)]

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
    start = 1
    count = 5
    x = list(range(start, start+count))
    y = generate_numbers_with_variation(start, start+count)
    figure = {
        'data': [
            go.Scatter(
                x=x,
                y=y,
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
