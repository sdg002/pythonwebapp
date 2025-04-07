import os
import dash
from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd

dash.register_page(
    __name__, title=f'Spinner ({os.environ.get("ENVIRONMENT")})')


def generate_data() -> pd.DataFrame:
    # Create a DataFrame with two columns: X and Y
    data = {
        'X': [1, 2, 3, 4, 5, 6],
        'Y': [10, 11, 12, 13, 14, 15]
    }
    df = pd.DataFrame(data)
    return df


def layout() -> object:
    df = generate_data()
    graph_element = dcc.Graph(
        id='spinner-graph',
        figure={
            'data': [
                go.Scatter(
                    x=df['X'],
                    y=df['Y'],
                    mode='lines+markers',
                    name='Line 1'
                )
            ],
            'layout': {
                'title': 'Dash Plotly Line Chart Example'
            }
        }
    )

    html_elements = html.Div([
        html.H1('Demonstrate spinner with chart'),
        graph_element,
    ])
    return html_elements
