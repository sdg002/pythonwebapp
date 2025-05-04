import logging
import time
import datetime as dt
import os
import dash
from dash import html, dcc
from flask import g

dash.register_page(
    __name__, title=f'Cache demo ({os.environ.get("ENVIRONMENT")})', order=7)


@dash.callback(
    dash.Output('selected-item-output', 'children'),
    dash.Input('id-items', 'value'))
def update_drop_down(country: str):
    logging.info(f"Inside update_dislay {country}")
    return country


@g.cache.cached(timeout=30)
def some_long_running_function_to_generate_data() -> list[str]:
    logging.info("Begin-generate_data")
    items = []
    count = 3
    for _ in range(count):
        items.append(dt.datetime.now())
        time.sleep(1.5)
    logging.info("End-generate_data")
    return items


def layout():
    logging.info(f"Inside layout function of {__file__}")
    items = some_long_running_function_to_generate_data()
    output_layout = [html.Span("Selected item:"),
                     html.Span(id='selected-item-output'),]
    how_to_use_this_page = [
        html.Li("Load this page"),
        html.Li("Take note of the first item. This has the time stamp"),
        html.Li("Keep refreshing every few seconds for "),
        html.Li("On subsequent page loads, the drop down items will remain unchanged"),
        html.Li("After about 30 seconds the cache will expire and "
                "you will see fresh items in the drop down")]
    html_elements = html.Div([
        html.H1('This is a page with Drop down whose items are retrieved from cache'),
        html.Div('Select an item.'),
        dcc.Dropdown(items, 'Canada', id='id-items'),
        html.Div(children=output_layout),
        html.H1("How to test this page"),
        html.Ol(children=how_to_use_this_page)
    ])
    return html_elements
