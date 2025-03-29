from flask import Flask
import dash_bootstrap_components as dbc
import logging
import dash
from dash import Dash, html, dcc
from flask import g


class DashHelper:

    @classmethod
    def register_dash_using_nav_bar(cls, flask_app: Flask):
        logging.info("Inside register_dash_using_nav")
        dash_app = Dash(use_pages=True, server=flask_app,
                        url_base_pathname="/dash/", external_stylesheets=[dbc.themes.BOOTSTRAP])
        nav_bar_links = []
        for page in dash.page_registry.values():
            logging.info(f"Found dash page {page['path']}")
            nav_item = dbc.NavLink(page["name"], href=page["relative_path"])
            nav_bar_links.append(nav_item)
        nav_bar_links.append(dbc.NavLink(
            "Back to root landing page", href="/", external_link=True))

        links_container = dbc.Nav(nav_bar_links)
        bootstrap_navbar = dbc.Navbar(
            links_container, color="primary", sticky="top", dark=True)

        dash_app.layout = html.Div([
            dcc.Location(id='url', refresh=False),
            bootstrap_navbar,
            dash.page_container
        ])
        logging.info("Register dash complete")
        return dash_app

    @classmethod
    def register_dash_using_nav(cls, flask_app: Flask):
        logging.info("Inside register_dash_using_nav")
        dash_app = Dash(use_pages=True, server=flask_app,
                        url_base_pathname="/dash/", external_stylesheets=[dbc.themes.BOOTSTRAP])
        nav_bar_links = []
        for page in dash.page_registry.values():
            logging.info(f"Found dash page {page['path']}")
            nav_item = dbc.NavLink(page["name"], href=page["relative_path"])
            nav_bar_links.append(nav_item)
        nav_bar_links.append(dbc.NavLink(
            "Back to root landing page", href="/", external_link=True))
        bootstrap_navbar = dbc.Nav(nav_bar_links)

        dash_app.layout = html.Div([
            dcc.Location(id='url', refresh=False),
            bootstrap_navbar,
            dash.page_container
        ])
        logging.info("Register dash complete")
        return dash_app

    @classmethod
    def register_dash_using_simple_navigation(cls, flask_app: Flask) -> Dash:
        logging.info("Inside register_dash_using_simple_navigation")
        dash_app = Dash(use_pages=True, server=flask_app,
                        url_base_pathname="/dash/", external_stylesheets=[dbc.themes.BOOTSTRAP])

        nav_bar_links = []
        for page in dash.page_registry.values():
            logging.info(f"Found dash page {page['path']}")
            nav_item = dbc.NavItem(dbc.NavLink(
                page["name"], href=page["relative_path"]))
            nav_bar_links.append(nav_item)
        # nav_bar_links.append(dbc.NavLink("Back to root landing page", href="/"))
        # Paths that aren't prefixed with requests_pathname_prefix are not supported.
        bootstrap_navbar = dbc.NavbarSimple(
            children=nav_bar_links,
            brand="My App",
            color="primary",
            dark=False,
            sticky="top",
            links_left=True,
            brand_href="/",
            brand_external_link=True)

        # nav_bar_links.append(html.Span(" | "))
        # nav_bar_links.append(html.A("Back to root landing page", href="/"))

        # banner=f'Multi-page app with Dash Pages ({os.environ.get("ENVIRONMENT")})'
        dash_app.layout = html.Div([
            dcc.Location(id='url', refresh=False),
            bootstrap_navbar,
            dash.page_container
        ])
        logging.info("Register dash complete")
        return dash_app
