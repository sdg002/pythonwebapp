import os
import logging
import random
import dash
from dash import dcc, html
import plotly.graph_objs as go

THEME_OPTIONS = [
    'plotly',
    'plotly_white',
    'plotly_dark',
    'ggplot2',
    'seaborn',
    'simple_white',
    'presentation',
    'xgridoff',
    'ygridoff',
]

dash.register_page(__name__, path='/plotlythemes',
                   title=f'Plotly Themes ({os.environ.get("ENVIRONMENT")})', order=8)


def build_figure(theme_name: str) -> go.Figure:
    x_values = list(range(1, 11))
    y_values = [random.randint(10, 100) for _ in x_values]

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
    return figure


@dash.callback(
    dash.Output('random-line-chart', 'figure'),
    dash.Output('selected-theme-name', 'children'),
    dash.Input('theme-dropdown', 'value'),
)
def update_chart_theme(theme_name: str):
    return build_figure(theme_name), f'This chart uses the Plotly theme: {theme_name}.'


def layout():
    logging.info('Page handler:{__name__}')
    theme_name = 'plotly_dark'

    html_elements = html.Div([
        html.H1('This is our Plotly Themes page'),
        html.Div('Choose a Plotly theme from the dropdown.'),
        dcc.Dropdown(
            options=[{'label': theme, 'value': theme}
                     for theme in THEME_OPTIONS],
            value=theme_name,
            id='theme-dropdown',
            clearable=False,
        ),
        html.Div(
            f'This chart uses the Plotly theme: {theme_name}.', id='selected-theme-name'),
        dcc.Graph(id='random-line-chart', figure=build_figure(theme_name)),
        html.A('Go back to the landing page', href='/'),
    ])
    return html_elements
