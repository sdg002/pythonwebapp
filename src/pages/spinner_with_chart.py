import logging
import time
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
import dash_html_components as html


dash.register_page(
    __name__, title=f'Spinner ({os.environ.get("ENVIRONMENT")})')


# def generate_data() -> pd.DataFrame:
#     # Create a DataFrame with two columns: X and Y
#     data = {
#         'X': [1, 2, 3, 4, 5, 6],
#         'Y': [10, 11, 12, 13, 14, 15]
#     }
#     df = pd.DataFrame(data)
#     time.sleep(4)
#     return df


def layout() -> object:
    elements = html.Div(children=[
        html.H1(children='Loading Example'),

        dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading-output-1")
        ),

        dcc.Interval(
            id='interval-component',
            interval=1*1000,  # in milliseconds
            n_intervals=0,
            max_intervals=1
        )
    ])
    return elements

# Define the callback to update the chart


# Define the callback to update the chart
@dash.callback(
    Output('loading-output-1', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    # Simulate a long computation
    logging.info(f"Interval triggered: {n}")
    time.sleep(5)

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

    return dcc.Graph(
        id='example-graph',
        figure=figure
    )


# def layout001() -> object:
#     df = generate_data()
#     graph_element = dcc.Graph(
#         id='spinner-graph',
#         figure={
#             'data': [
#                 go.Scatter(
#                     x=df['X'],
#                     y=df['Y'],
#                     mode='lines+markers',
#                     name='Line 1'
#                 )
#             ],
#             'layout': {
#                 'title': 'Dash Plotly Line Chart Example'
#             }
#         }
#     )

#     html_elements = html.Div([
#         html.H1('Demonstrate spinner with chart'),
#         graph_element,
#     ])
#     return html_elements
