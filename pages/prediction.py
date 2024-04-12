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

def create_pred_fig(df, trace_add=True):
    fig = go.Figure()

    sample_df = pd.DataFrame({
        "longitude": None,
        "latitude": None
    }, index=[0])

    if trace_add:

        fig.add_trace(go.Scattergeo(
            lat=df["latitude"].astype(float),
            lon=df["longitude"].astype(float),
            mode='markers',
            marker=dict(color='rgba(102, 102, 102)', 
                        size=10, line = dict(width=3,
			color='rgba(68, 68, 68, 0)')),
            hoverinfo='none'
        ))

    fig.update_layout(
        paper_bgcolor='#EAECEF',
        plot_bgcolor='#EAECEF',
        geo = dict(
            scope='north america',
            showland = True,
            projection_scale=2, #this is kind of like zoom
            center=dict(lat=43, lon=-110.116226),
            landcolor = "#f0e8e4",
            subunitcolor = "#fc6603",
            countrycolor = "#fc6603",
            countrywidth = 0.8,
            subunitwidth = 0.5
        )
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
    )
    
    return fig

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
        dbc.Alert(["Please make sure to include Longitude and Latitude as a numeric data type."],
                  id="alert-fade",
                    dismissable=True,
                    is_open=True,
                    fade=True,
                    color="warning"),
        dbc.Card(
                dbc.CardBody([
                    html.P("Your Input is: "),
                    html.Div(id="user_inputs"),
                    html.Hr(),
                    dcc.Graph(
                        id='pred_map',
                        figure=create_pred_fig(None, trace_add=False)),
                    html.Div(id="prediction_card")], 
                    style={"text-align":"center", "margin-right": "20px"}),
                className="mb-4", color="light"
            )
        ], style={"margin-right": "20px"})

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
    [Output("prediction_card", "children"),
     Output("user_inputs", "children"),
     Output("pred_map", "figure")],
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
        {"longitude": float(longitude_input),
         "latitude": float(latitude_input),
         "accommodates": people_dropdown_eval,
         "room_type": roomtype_dropdown_eval,
         "beds": float(num_beds_dropdown_eval),
         "bathroom_adjusted": float(num_bathrooms_dropdown_eval)},
         index=[0]
    )
    if "eval_button" == ctx.triggered_id:

        inputs = f"Longitude: {longitude_input}, \
            \n Latitude: {latitude_input}, \n Number of Guests: {people_dropdown_eval}, \n Room Type: {roomtype_dropdown_eval}, \n Number of Beds: {num_beds_dropdown_eval}, \n Number of Bathrooms: {num_bathrooms_dropdown_eval}"

        pred_val = predict_price(new_df)

        new_df["pred_val"] = pred_val

        pred_alert = [
        html.P(f"Your Predicted Value per Night is: ${pred_val[0]:.3f} CAD.", style={'fontSize': '13px'})
        ]

        pred_edited_fig = create_pred_fig(new_df)
        return pred_alert, inputs, pred_edited_fig
