import logging
from flask import Flask
import dash_bootstrap_components as dbc
import dash
from dash import Dash, Input, Output, callback, html, dcc
# from dash.dependencies import Input, Output


class DashHelper:

    @classmethod
    def register_dash_using_tabs(cls, flask_app: Flask):
        logging.info("Inside register_dash_using_tabs")
        dash_app = Dash(use_pages=True, server=flask_app,
                        prevent_initial_callbacks=True,
                        url_base_pathname="/dash/")
        tab_children = []
        for page in dash.page_registry.values():
            page_name = page["name"]
            # page_path = page['path']
            relative_path = page["relative_path"]
            tab_children.append(
                dcc.Tab(label=page_name, value=relative_path))

        tabs = dcc.Tabs(
            id="tabs",
            value="tab-1",
            children=tab_children,
            persistence_type="session", persistence=True)

        dash_app.layout = html.Div([
            tabs,
            dcc.Location(id='url'),
            dash.page_container
        ])
        logging.info("Register dash complete")
        return dash_app

    @classmethod
    def register_dash_using_nav_bar(cls, flask_app: Flask):
        logging.info("Inside register_dash_using_nav")
        dash_app = Dash(use_pages=True, server=flask_app,
                        prevent_initial_callbacks=True,
                        url_base_pathname="/dash/", external_stylesheets=[dbc.themes.BOOTSTRAP])
        nav_bar_links = []
        for page in dash.page_registry.values():
            logging.info(
                f"Found dash page path={page['path']} , relative_path={page['relative_path']}")
            nav_item = dbc.NavLink(page["name"], href=page["relative_path"])
            nav_bar_links.append(nav_item)

        nav_bar_links.append(dbc.NavLink(
            "Back to root landing page", href="/", external_link=True))

        links_container = dbc.Nav(nav_bar_links, pills=True)
        bootstrap_navbar = dbc.Navbar(
            links_container, color="primary", sticky="top", dark=True)
        # color="light", "default" was not good. The text in the links did not show up at all

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

        # banner=f'Multi-page app with Dash Pages ({os.environ.get("ENVIRONMENT")})'
        dash_app.layout = html.Div([
            dcc.Location(id='url'),
            bootstrap_navbar,
            dash.page_container
        ])
        logging.info("Register dash complete")
        return dash_app

    # Callback is fired, cannot be a class method
    # But, you will have to return the a tuple of CSS class names for all the nav items
    # Challenge - it becomes a complex if-else statement to determine which nav item is active
    # @dash.callback([dash.Input('url', 'pathname')])
    # def update_active_link(pathname: str) -> str:
    #     logging.info(f"Inside update_active_link with pathname={pathname}")
    #     # Update the active link based on the current pathname
    #     for page in dash.page_registry.values():
    #         if pathname == page["relative_path"]:
    #             return page["name"]


@callback(Output('url', 'pathname'),
          Input('tabs', 'value'),
          prevent_initial_call=True)
def route(tab_value):
    logging.info(f"Inside route handler with tab_value={tab_value}")
    return tab_value
