import dash
from dash import html,dcc
import logging
import lib
import datetime as dt
import time

dash.register_page(__name__)

@dash.callback(
    dash.Output('selected-item-output', 'children'),
    dash.Input('id-items', 'value'))
def update_drop_down(country: str):
    logging.info(f"Inside update_dislay {country}")
    return country

@lib.FLASK_CACHE.cached(timeout=30)
def some_long_running_function_to_generate_data()->list[str]:
    logging.info("Begin-generate_data")
    items=[]
    count = 3
    for idx in range(count):
        items.append(dt.datetime.now())
        time.sleep(1.5)
    logging.info("End-generate_data")
    return items

def layout():
    logging.info(f"Inside layout function of {__file__}")
    items=some_long_running_function_to_generate_data()
    output_layout=[html.Span("Selected item:"),html.Span(id='selected-item-output'),]
    layout = html.Div([
        html.H1('This is a page with Drop down whose items are retrieved from cache'),
        html.Div('Select an item.'),
        dcc.Dropdown(items, 'Canada', id='id-items'),
        html.Div(children=output_layout),
    ])
    return layout
