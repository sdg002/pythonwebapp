import os
import logging
import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__, name="top1",  title=f'top1  ({os.environ.get("ENVIRONMENT")})', order=1)


def layout():
    logging.info(f'Page handler:{__name__}')
    return html.Div([
        html.H1('This is Top 1 page - display Tabs here'),])
