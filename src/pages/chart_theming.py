import os
import logging
import random
import dash
from dash import dcc, html
import plotly.graph_objs as go

dash.register_page(__name__, path='/plotlythemes',
                   title=f'Plotly Themes ({os.environ.get("ENVIRONMENT")})', order=8)


def layout():
    logging.info('Page handler:{__name__}')
    x_values = list(range(1, 11))
    y_values = [random.randint(10, 100) for _ in x_values]
    theme_name = 'plotly_dark'

    figure = go.Figure(
        data=[go.Scatter(x=x_values, y=y_values,
                         mode='lines+markers', name='Random values')]
    )
    figure.update_layout(
        title='Simple Plotly Line Chart',
        xaxis_title='X',
        yaxis_title='Y',
        template=theme_name,
    )

    html_elements = html.Div([
        html.H1('This is our Plotly Themes page'),
        html.Div(f'This chart uses the Plotly theme: {theme_name}.'),
        dcc.Graph(id='random-line-chart', figure=figure),
        html.A('Go back to the landing page', href='/'),
    ])
    return html_elements
