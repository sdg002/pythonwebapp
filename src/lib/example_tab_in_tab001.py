import logging
from flask import Flask
import dash_bootstrap_components as dbc
import dash
from dash import Dash, Input, Output, callback, html, dcc


class ExampleDashHelper:
    """
    Helper class to register a multi-level tabbed Dash app
    """
    @classmethod
    def register_dash_using_tabs(cls, flask_app: Flask):
        logging.info("Inside register_dash_using_tabs")
        dash_app = Dash(use_pages=True, server=flask_app,
                        prevent_initial_callbacks=True,
                        url_base_pathname="/dash/")

        # Define the first-level tabs
        first_level_tabs = [
            {"label": "Tab Group 001", "value": "group-1"},
            {"label": "Tab Group 002", "value": "group-2"}
        ]

        # Define the second-level tabs for each group
        second_level_tabs = {
            "group-1": [
                {"label": "Tab 1.1", "value": "tab-1-1"},
                {"label": "Tab 1.2", "value": "tab-1-2"}
            ],
            "group-2": [
                {"label": "Tab 2.1", "value": "tab-2-1"},
                {"label": "Tab 2.2", "value": "tab-2-2"}
            ]
        }

        # Layout with two levels of tabs
        dash_app.layout = html.Div([
            dcc.Tabs(
                id="first-level-tabs",
                value="group-1",
                children=[
                    dcc.Tab(label=tab["label"], value=tab["value"])
                    for tab in first_level_tabs
                ]
            ),
            html.Div(id="second-level-tabs-container"),
            html.Div(id="tab-content"),
            dash.page_container
        ])

        # Callback to dynamically render second-level tabs based on the first-level tab selection
        @dash_app.callback(
            Output("second-level-tabs-container", "children"),
            Input("first-level-tabs", "value")
        )
        def update_second_level_tabs(selected_group):
            return dcc.Tabs(
                id="second-level-tabs",
                value=second_level_tabs[selected_group][0]["value"],
                children=[
                    dcc.Tab(label=tab["label"], value=tab["value"])
                    for tab in second_level_tabs[selected_group]
                ]
            )

        # Callback to update content based on the second-level tab selection
        @dash_app.callback(
            Output("tab-content", "children"),
            Input("second-level-tabs", "value")
        )
        def update_tab_content(selected_tab):
            return html.Div(f"Content for {selected_tab}")

        logging.info("Register dash complete")
        return dash_app
