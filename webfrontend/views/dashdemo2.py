import dash as dash

class DashDemo2(object):
    """Container class to hodl the Dash entry point methods"""
    @classmethod
    def make_dash(cls, server):
        d=dash.Dash(
            server=server,
            url_base_pathname='/dash2/', title="Dash demo 2"
        )
        d.layout = cls.make_layout
        cls.define_callbacks()
        return d

    @classmethod    
    def make_layout(cls):
        return dash.html.Div(                                                                                                                                                                                                 
            [   
                dash.html.A("Home",href='/', title="Click to go back to Home"),
                dash.html.Hr(),                                                                                                                                                                                 
                dash.html.P("Hey this is a demo Dash app 2. Type something in the text box:)"),                                                                                                                                                                     
                dash.dcc.Input(id="input"),                                                                                                                                                                                   
                dash.html.Div(id="output"),                                                                                                                                                                                   
            ]                                                                                                                                                                                                            
        )
    
    @classmethod
    def define_callbacks(cls):
        @dash.callback(
            dash.Output("output", "children"),
            dash.Input("input", "value"),
        )
        def show_output(text):
            return f"you entered: '{text}'"





    