import os
import logging
import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__, name="Radio buttons",  title=f'Radio buttons ({os.environ.get("ENVIRONMENT")})', order=2)


def layout():
    logging.info(f'Page handler:{__name__}')
    html_elements = html.Div([
        html.H1('This is a demo of Radio buttons'),
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
    return html_elements


@callback(
    Output('analytics-output', 'children'),
    Input('analytics-input', 'value')
)
def update_city_selected(input_value):
    return f'You selected: {input_value}'
