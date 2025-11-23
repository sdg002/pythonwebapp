import logging
from flask import Flask
import dash_bootstrap_components as dbc
import dash
from dash import Dash, Input, Output, callback, html, dcc


class ExampleNavBarTab002:
    def __init__(self):
        pass

    @classmethod
    def register_dash_using_simple_navigation(cls, flask_app: Flask) -> Dash:
        logging.info("Inside register_dash_using_simple_navigation")
        dash_app = Dash(use_pages=True, server=flask_app,
                        url_base_pathname="/dash/", external_stylesheets=[dbc.themes.BOOTSTRAP])

        nav_bar_links = []
        top_level_pages = [("Top 1", "/dash/top1"), ("Top 2", "/dash/top2")]
        for name, path in top_level_pages:
            logging.info(f"Adding nav link for page {path}")
            nav_item = dbc.NavItem(dbc.NavLink(
                name, href=path))
            nav_bar_links.append(nav_item)
        # for page in dash.page_registry.values():
        #     logging.info(f"Found dash page {page['path']}")
        #     nav_item = dbc.NavItem(dbc.NavLink(
        #         page["name"], href=page["relative_path"]))
        #     nav_bar_links.append(nav_item)
        bootstrap_navbar = dbc.NavbarSimple(
            children=nav_bar_links,
            brand="My App",
            color="primary",
            dark=False,
            sticky="top",
            links_left=True,
            brand_href="/",
            brand_external_link=True)

        # banner=f'Multi-page app with Dash Pages ({os.environ.get("ENVIRONMENT")})'
        dash_app.layout = html.Div([
            dcc.Location(id='url'),
            bootstrap_navbar,
            dash.page_container
        ])
        logging.info("Register dash complete")
        return dash_app
