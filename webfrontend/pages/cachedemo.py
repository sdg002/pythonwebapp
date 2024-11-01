import dash
from dash import html,dcc
import logging

dash.register_page(__name__)

@dash.callback(
    dash.Output('selected-item-output', 'children'),
    dash.Input('id-items', 'value'))
def update_drop_down(country: str):
    logging.info(f"Inside update_dislay {country}")
    return country


def layout():
    logging.info(f"Inside layout function of {__file__}")
    items=["USA","UK", "Canada" ,"France"]
    output_layout=[html.Span("Selected item:"),html.Span(id='selected-item-output'),]
    layout = html.Div([
        html.H1('This is a page with Drop down whose items are retrieved from cache'),
        html.Div('Select an item.'),
        dcc.Dropdown(items, 'Canada', id='id-items'),
        html.Div(children=output_layout),
    ])
    return layout
