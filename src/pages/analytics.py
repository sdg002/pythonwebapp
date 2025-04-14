import os
import logging
import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__, title=f'Analytics ({os.environ.get("ENVIRONMENT")})')


def layout():
    logging.info(f"Inside handler:{__name__}")
    html_element = html.Div([
        html.H1('This is our Analytics page'),
        html.Div([
            "Select a city: ",
            dcc.RadioItems(
                options=['New York City', 'Montreal', 'San Francisco'],
                value='Montreal',
                id='analytics-input'
            )
        ]),
        html.Br(),
        html.Div(id='analytics-output'),
    ])
    return html_element


@callback(
    Output('analytics-output', 'children'),
    Input('analytics-input', 'value')
)
def update_city_selected(input_value):
    return f'You selected: {input_value}'
