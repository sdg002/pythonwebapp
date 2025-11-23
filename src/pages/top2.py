import os
import logging
import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__, name="top2",  title=f'top2  ({os.environ.get("ENVIRONMENT")})', order=2)


def layout():
    logging.info(f'Page handler:{__name__}')
    return html.Div([
        html.H1('This is Top 2 page - display Tabs here'),])
