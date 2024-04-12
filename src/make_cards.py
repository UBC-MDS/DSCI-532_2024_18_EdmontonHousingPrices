from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from dash import Dash, html, dcc, dash_table, ctx

import plotly.graph_objects as go

fig = go.Figure()

dash.register_page(__name__, path="/", title="Credentials")

def make_card(photo, name, description, fontsize):
    card = dbc.Card([
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src=f"assets/{photo}.png",
                        className="img-fluid rounded-start",
                        style={'height': '130px', 'width': '130px', 'object-fit': 'contain'},
                    ),
                    className="col-md-3", 
                    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4(name, className="card-title"),
                            html.P(
                                description,
                                className="card-text",
                                style={"fontSize": fontsize}
                            ),
                        ]
                    ),
                    className="col-md-9",  
                ),
            ],
            className="g-0 align-items-center",
            style={'height': '150px'}, 
        ),
    ],
    color="primary", outline=True,
    className="mb-3",
    style={"maxWidth": "700px"},
    )
    return card