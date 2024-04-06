import sys
sys.path.append('../')

from dash import html
import dash_bootstrap_components as dbc
import menu
import dash
from dash import dcc
from dash.dependencies import Input, Output, State
from app import app
from dash import Dash, html, dcc, dash_table, ctx
from dash import callback_context
import numpy as np

from assets.texts import jenny, wenyu

import plotly.graph_objects as go

import pandas as pd

fig = go.Figure()

dash.register_page(__name__, path="/", title="Credentials")

def make_card(photo, name, description):
      card = dbc.Card([
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src=f"assets/{photo}.png",
                        className="img-fluid rounded-start",
                        style={'height':'150px', 
                               'width':'150px',
                               "text-align": "center",
                               "top": 0, "left": 50,
                               "align":"center",}
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4(f"{name}", className="card-title"),
                            html.P(
                                description
                            ),                            
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        ),
    ],
    color="primary", outline=True,
    className="mb-3",
    style={"maxWidth": "700px", "height": "150px"},
      )
      return card

maindiv = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H4("Meet the Team"), style={'display': 'inline-block',
                                                 "text-align": "left",
                                                 "color": "#d85e30",
                                                #  "font-family": "Arial, sans-serif",
                                                 "font-weight": "italic"},
                                                 align="top", width=3
            ),
            dbc.Col([
                  html.P(
                        "We are group of data science students enrolled in Master of Data Science program."
                  ),
                  make_card(jenny[1], jenny[0], jenny[2]),
                  make_card(wenyu[1], wenyu[0], wenyu[2]),
                  make_card(jenny[1], jenny[0], jenny[2]),
                  make_card(jenny[1], jenny[0], jenny[2])
        ])
        ]),
         html.Hr(),
         dbc.Row([
            dbc.Col(
                html.H4("Inspiration"), style={'display': 'inline-block',
                                                 "text-align": "left",
                                                 "color": "#d85e30",
                                                #  "font-family": "Arial, sans-serif",
                                                 "font-weight": "bold"},
                                                 align="top", width=3
            ),
            dbc.Col([
                        html.P(
                            "This dashboard, created by a team of Master of Data Science students, offers a comprehensive and interactive platform designed to assist Airbnb hosts in Vancouver with pricing their listings. Drawing from a rich dataset of eight years of Airbnb listings in the city, our app provides a deep dive into various aspects of the rental market, from geographical trends to detailed property features."
                        ),
                        html.P(
                            "Key features of the dashboard include: An interactive map highlighting the price range in different Vancouver neighborhoods, detailed filters allowing users to customize their search based on property type, number of bedrooms, and more, visualization of historical data on rental prices, offering insights into market trends, and a predictive model to help hosts estimate appropriate pricing for their listings."
                        ),
                        html.P(
                            "Whether you are an existing Airbnb host or planning to list your property, our dashboard is tailored to provide valuable insights and predictions to help you navigate the dynamic rental landscape in Vancouver."
                        ),
                        html.P(
                            "For more details, access",
                            style={'display': 'inline-block',
                                "text-align": "left",
                                "color": "#000000",
                                "font-weight": "bold"}
                        ),
                        html.A(
                            " our repository",
                            href="https://github.com/UBC-MDS/DSCI-532_2024_18_VancouverAirbnbPrices"
                        ),
                        html.Br(),
                        html.P(
                            "Latest Update: 2024-04-05", 
                            style={'display': 'inline-block',
                                "text-align": "left",
                                "color": "#000000",
                                "font-weight": "bold"}
                        )
                    ])
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                html.H4("References"), style={'display': 'inline-block',
                                                 "text-align": "left",
                                                 "color": "#d85e30",
                                                #  "font-family": "Arial, sans-serif",
                                                 "font-weight": "bold"},
                                                 align="top", width=3
            ),
            dbc.Col([
                  html.Ul([
                        html.Li("This is where the credentials go"),
                        html.Li("Okay Sure")
                  ], id='credential-list')

        ])
        ])
    ]),

])


layout = html.Div(children=[
    menu.dropdown_menu,

    dbc.Row([
        dbc.Col(maindiv)  
    ])
])