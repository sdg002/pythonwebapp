import logging
import os
import dash
from dash import html, dcc

# 2 buttons - 1 does something good , 2nd throws exception
# handle the exception in the call back and display a nicely formatted error message
# try to reuse make the error handler a reusable function (return a html layout wiht the error message)
# you were here

dash.register_page(
    __name__, title=f'Error handler demo ({os.environ.get("ENVIRONMENT")})', order=50)


def layout():
    logging.info('CentrallPage handler:{__name__}')
    html_elements = html.Div([
        html.H1('Error handler demo'),
        html.Div('This is page content.. to be done.'),
    ])
    return html_elements
