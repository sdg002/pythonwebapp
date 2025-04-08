import os
import dash
from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd
import time
from dash.dependencies import Input, Output
import dash_html_components as html


dash.register_page(
    __name__, title=f'Spinner ({os.environ.get("ENVIRONMENT")})')


def generate_data() -> pd.DataFrame:
    # Create a DataFrame with two columns: X and Y
    data = {
        'X': [1, 2, 3, 4, 5, 6],
        'Y': [10, 11, 12, 13, 14, 15]
    }
    df = pd.DataFrame(data)
    time.sleep(4)
    return df


def layout() -> object:
    loading_element = dcc.Loading(
        id="loading-1",
        type="default",
        show_initially=True,
        children=html.Div(id="loading-output-1")
    )
    interval_element = dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
    html_elements = html.Div([
        html.H1(children='Loading Example'),
        loading_element,
        interval_element])
    return html_elements

# Define the callback to update the chart


@dash.callback(
    Output('loading-output-1', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    # Simulate a long computation
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
