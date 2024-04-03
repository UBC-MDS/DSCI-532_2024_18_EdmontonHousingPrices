from dash import html
import dash
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import Input, Output, State
import os

dropdown_menu = dbc.Navbar(
    dbc.Container([dbc.Row([
                        dbc.Col([
                            html.Img(src=dash.get_asset_url('house_icon.png'), height="35px"),
                            dbc.NavbarBrand("Vancouver AirBnB Listings", className="ms-2")
                        ],
                        width={"size":"auto"}, className="g-0"),
                    ],
                    align="center",
                    className="ml-0"),

        dbc.Row([
            dbc.Col([
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Observation", href="/")),
                    dbc.NavItem(dbc.NavLink("Prediction", href="/prediction")),
                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi-github"),
                                            href="https://github.com/UBC-MDS/DSCI-532_2024_18_VancouverAirbnbPrices",
                                            external_link=True)),
                ], navbar=True)
            ], align="center", className="ml-auto"),

        ]),
    ]),
    color="primary",
    dark=True,
    className="mb-3",
)