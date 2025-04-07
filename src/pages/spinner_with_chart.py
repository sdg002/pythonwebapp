import os
import dash
from dash import html, dcc
import plotly.graph_objs as go


dash.register_page(
    __name__, title=f'Spinner ({os.environ.get("ENVIRONMENT")})')


def layout() -> object:
    graph_element = dcc.Graph(
        id='spinner-graph',
        figure={
            'data': [
                go.Scatter(
                    x=[1, 2, 3, 4, 5],
                    y=[10, 11, 12, 13, 14],
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
