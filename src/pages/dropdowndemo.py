import logging
import os
import dash
from dash import html, dcc

dash.register_page(
    __name__, name="Dropdown persistence", title=f'Dropdown demo ({os.environ.get("ENVIRONMENT")})', order=4)


@dash.callback(
    dash.Output('country-output', 'children'),
    dash.Input('id-dropdown-country', 'value'))
def update_display(country: str):
    logging.info(f"Drop down - callback {country}")
    return country


def layout():
    logging.info("Inside layout function")
    countres = ["USA", "UK", "Canada", "France"]
    output_layout = [html.Span("Selected country:"),
                     html.Span(id='country-output'),]
    html_elements = html.Div([
        html.H1('This is a page with Drop down'),
        html.Div('Select a country.'),
        dcc.Dropdown(
            countres,
            'Canada', 
            id='id-dropdown-country',
            persistence=True,
            persistence_type='local'),
        html.Div(children=output_layout),
    ])
    return html_elements
