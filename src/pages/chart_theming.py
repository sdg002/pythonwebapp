import os
import logging
import random
import dash
from dash import dcc, html
import plotly.graph_objs as go
import plotly.io as pio

CUSTOM_THEME_NAME = 'custom_blue_slate'


def register_custom_theme() -> None:
    custom_theme = go.layout.Template(
        layout=go.Layout(
            paper_bgcolor='#f7fafc',
            plot_bgcolor='#ffffff',
            font={'family': 'Verdana, sans-serif',
                  'size': 14, 'color': '#1f2937'},
            title={'font': {'size': 22, 'color': '#0f172a'}},
            xaxis={'gridcolor': '#dbe3ef', 'zerolinecolor': '#c5d0e0'},
            yaxis={'gridcolor': '#dbe3ef', 'zerolinecolor': '#c5d0e0'},
            colorway=['#2563eb', '#dc2626', '#16a34a', '#d97706', '#7c3aed'],
        )
    )
    pio.templates[CUSTOM_THEME_NAME] = custom_theme


register_custom_theme()

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
    CUSTOM_THEME_NAME,
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
    return build_figure(theme_name), [
        'This chart uses the Plotly theme: ',
        html.Strong(theme_name),
        '.',
    ]


def layout():
    logging.info('Page handler:{__name__}')
    theme_name = 'plotly_dark'

    html_elements = html.Div([
        html.H1('How to set a theme on the Plotly charts?'),
        dcc.Markdown(
            'This page generates a random line chart and lets you change its appearance by selecting a Plotly theme. '
            'When you pick a new theme, the chart updates immediately with the selected template.'
        ),
        html.Hr(),
        html.Div([
            html.Span('Choose a Plotly theme from the dropdown.'),
            dcc.Dropdown(
                options=[{'label': theme, 'value': theme}
                         for theme in THEME_OPTIONS],
                value=theme_name,
                id='theme-dropdown',
                clearable=False,
                style={'width': '220px'},
            ),
        ], style={'display': 'flex', 'alignItems': 'center', 'gap': '0.75rem'}),
        html.Hr(),
        html.Div(
            f'This chart uses the Plotly theme: {theme_name}.', id='selected-theme-name'),
        dcc.Graph(id='random-line-chart', figure=build_figure(theme_name)),
        html.A('Go back to the landing page', href='/'),
    ])
    return html_elements
