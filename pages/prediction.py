import sys
sys.path.append('../')

from dash import html
import dash_bootstrap_components as dbc
import menu
import dash
from dash import dcc
from dash.dependencies import Input, Output, State
from app import app
from dash import Dash, html, dcc, dash_table, ctx, callback
from dash import callback_context
import numpy as np
from src.predict import predict_price  ### This is the function for using model to predict

# from functions.visualization import map_fig

import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
dash.register_page(__name__, path="/", title="Prediction")

df = pd.read_csv("data/raw/listings.csv")
df = df[df["host_location"] == "Vancouver, Canada"]
df.dropna(subset=['host_location', 'price', 'bathrooms_text'], inplace=True)
df = df[["neighbourhood_cleansed", "accommodates", "price", "room_type", "beds", "bathrooms_text", "quarter"]]

df["price_adjusted"] = df["price"].str.extract(r'([0-9.]+)', expand = False).astype(float)
df["bathroom_adjusted"] = df["bathrooms_text"].str.extract(r'([0-9.]+)', expand = False).astype(float)

sidebar = html.Div([
        html.H4("Select Options", style={"margin-left": "14px"}),
        html.Hr(),
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.Label("Select Longitude:", style={"color": "black"}),
                    dbc.Input(id="longitude_input", placeholder="Enter in data type float", type="float", style={"margin-bottom": "20px"}),
                ])
            ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Select Latitude:", style={"color": "black"}),
                          dbc.Input(id="latitude_input", placeholder="Enter in data type float", type="float", style={"margin-bottom": "20px"})
                    ])
              ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Number of Guests:", style={"color": "black"}),
                          dcc.Dropdown(id="people_dropdown_eval",
                                       options=np.arange(start=1, stop=10, step=1).tolist(),
                                       multi=False,
                                       style={"margin-bottom": "20px"})
                    ])
              ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Room Type:", style={"color": "black"}),
                          dcc.Dropdown(id="roomtype_dropdown_eval",
                                       options=[{"label": r, "value": r} for r in df["room_type"].unique().tolist()],
                                       multi=False,
                                       style={"margin-bottom": "20px"})
                    ])
              ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Number of Beds:", style={"color": "black"}),
                          dcc.Dropdown(id="num_beds_dropdown_eval",
                                       options=np.arange(start=1, stop=10, step=1).tolist(),
                                       multi=False,
                                       style={"margin-bottom": "20px"})
                    ])
              ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Number of Bathrooms:", style={"color": "black"}),
                          dcc.Dropdown(id="num_bathrooms_dropdown_eval",
                                       options=np.arange(start=0.5, stop=6, step=0.5).tolist(),
                                       multi=False,
                                       style={"margin-bottom": "20px"})
                    ])
              ]),

            dbc.Row([
                  dbc.Col([
                        dbc.ButtonGroup([
                              dbc.Button("Get Evaluation", id="eval_button", n_clicks=0, style={'textAlign':'center'})])
                  ],  align="center", style={'display': 'flex', 'justify-content': 'center'})
            ], justify="center")

        ])
])

maindiv = html.Div(
    id="first-div",
    children=[
        html.Div([
        html.H4("Predicted Price per Night (CAD)"),
        html.Hr(),
        html.Div(id="display_pred", style={"margin-right":"20px"})
        ]),

    ]
)

layout = html.Div(children=[
    menu.dropdown_menu,

    dbc.Row([
        dbc.Col(sidebar, width=3), 
        dbc.Col(maindiv, width=9)  
    ])
])

@app.callback(
    [Output("display_pred", "children")],
    [Input('eval_button', 'n_clicks'),
     State("people_dropdown_eval", "value"),
     State("roomtype_dropdown_eval", "value"),
     State("num_beds_dropdown_eval", "value"),
     State("num_bathrooms_dropdown_eval", "value"),
     State("longitude_input", "value"),
     State("latitude_input", "value")]
)
def getOptionValues(eval_button, people_dropdown_eval, 
                    roomtype_dropdown_eval, 
                    num_beds_dropdown_eval, 
                    num_bathrooms_dropdown_eval,
                    latitude_input, longitude_input):
    statement = "Hi"
    new_df = pd.DataFrame(
        {"latitude": float(latitude_input),
         "longitude": float(longitude_input),
         "room_type": roomtype_dropdown_eval,
         "num_guests": people_dropdown_eval,
         "num_beds": num_beds_dropdown_eval,
         "num_baths": num_bathrooms_dropdown_eval},
         index=[0]
    )
    if "eval_button" == ctx.triggered_id:
        print(latitude_input, longitude_input, roomtype_dropdown_eval, num_beds_dropdown_eval, people_dropdown_eval, num_bathrooms_dropdown_eval)

        pred_alert = [
        dbc.Card(
                dbc.CardBody([f"Your Input: ",
                              html.Hr(),
                              f"{longitude_input}"], 
                             style={"text-align":"center"}),
                className="mb-4", color="light"
            )
        ]

        # fig = px.scatter_mapbox(
        #     new_df, lat = new_df.latitude, lon = new_df.longitude,
        #     hover_name="num_guests", zoom=5
        # )
        pred = f"{longitude_input, longitude_input}"
        return pred_alert
