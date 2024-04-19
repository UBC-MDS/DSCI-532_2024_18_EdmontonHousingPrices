from dash import html
import dash
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import Input, Output, State
import os

dropdown_menu = dbc.Navbar(
    dbc.Container([dbc.Row([
                        dbc.Col([
                            html.Img(src=dash.get_asset_url('house_icon_new.png'), height="30px", style={'margin-bottom': '8px'}),
                            dbc.NavbarBrand("Vancouver AirBnB Listings", className="ms-2", style={'margin-top': '20px',
                                                                                                  'margin-bottom': '20px',
                                                                                                  "margin-right":"2px"}),
                        ],
                        width={"size":"auto"}, className="g-0")
                    ],
                    align="right",
                    className="ml-0"),

        dbc.Row([
            dbc.Col([
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Observation", href="/")),
                    dbc.NavItem(dbc.NavLink("Prediction", href="/prediction")),
                    dbc.NavItem(dbc.NavLink("About", href="/credentials")),
                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi-github"),
                                            href="https://github.com/UBC-MDS/DSCI-532_2024_18_VancouverAirbnbPrices",
                                            external_link=True)),
                ], navbar=True)
            ], align="left", className="ml-auto", style={"margin-left":"auto"}),

        ]),
    ], fluid=True),
    color="primary",
    dark=True,
    className='px-3',
)