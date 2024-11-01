import dash
from dash import html,dcc
import logging

dash.register_page(__name__)

def layout():
    logging.info(f"Inside layout function of {__file__}")
    items=["USA","UK", "Canada" ,"France"]
    output_layout=[html.Span("Selected item:"),html.Span(id='country-output'),]
    layout = html.Div([
        html.H1('This is a page with Drop down whose items are retrieved from cache'),
        html.Div('Select an item.'),
        dcc.Dropdown(items, 'Canada', id='id-items'),
        html.Div(children=output_layout),
    ])
    return layout
