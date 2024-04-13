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
from src.map import create_map, create_empty_map, create_prediction_map

import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
dash.register_page(__name__, path="/", title="Prediction")

df = pd.read_csv("data/raw/listings.csv")
df = df[df["host_location"] == "Vancouver, Canada"]
df.dropna(subset=['host_location', 'price', 'bathrooms_text'], inplace=True)

df = df[["neighbourhood_cleansed", "accommodates", "price", "room_type", "beds", "bathrooms_text", "quarter","longitude", "latitude"]]

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

maindiv = html.Div([
    html.H4("Predicted Price per Night (CAD)"),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.P("You did not input any values yet.", id="input_statement"),
            html.Div(id="user_inputs"),
            html.Div(id="prediction_card")
        ]),
        dbc.Col([
            html.H5("View in Map"),
            html.Div([
                dbc.Card([
                    dcc.Graph(id="prediction_map", figure=create_empty_map(df))
                ])
            ], style={"margin-right":"20px"})
        ])
    ])
])

# maindiv = html.Div(
#     id="first-div",
#     children=[
#         html.Div([
#         html.H4("Predicted Price per Night (CAD)"),
#         html.Hr(),
#         html.P("You did not input any values yet.", id="input_statement"),
#         html.Div(id="user_inputs"),
#         html.Div(id="prediction_card")
#         # dbc.Card(
#         #         dbc.CardBody([
#         #             html.P("You did not input any values yet.", id="input_statement"),
#         #             html.Div(id="user_inputs"),
#         #             html.Div(id="prediction_card")], 
#         #             style={"text-align":"center", "margin-right": "10px"}),
#         #         className="mb-4", color="light"
#         #     )
#         ], style={"margin-right": "20px"}),

#         html.Div([
#         html.H4("View in Map"),
#         html.Hr(),
#         dbc.Card(
#             dbc.CardBody([
#                 dbc.Row([
#                     dbc.Col([
#                         dcc.Graph(id="prediction_map", figure=create_empty_map(df))
#                     ])
#                 ])
#             ]), 
#             className="mt-3"
#         )
#         ], style={"margin-right": "20px"}) 
#     ]
# )

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
     Output("input_statement", "children"),
     Output("prediction_map", "figure")],
    [Input('eval_button', 'n_clicks'),
     State("people_dropdown_eval", "value"),
     State("roomtype_dropdown_eval", "value"),
     State("num_beds_dropdown_eval", "value"),
     State("num_bathrooms_dropdown_eval", "value"),
     State("latitude_input", "value"),
     State("longitude_input", "value")]
)
def getOptionValues(n_clicks, people_dropdown_eval, 
                    roomtype_dropdown_eval, 
                    num_beds_dropdown_eval, 
                    num_bathrooms_dropdown_eval,
                    latitude_input, longitude_input):

    new_df = pd.DataFrame(
        {"longitude": float(longitude_input),
         "latitude": float(latitude_input),
         "accommodates": people_dropdown_eval,
         "room_type": roomtype_dropdown_eval,
         "beds": float(num_beds_dropdown_eval),
         "bathroom_adjusted": float(num_bathrooms_dropdown_eval)},
         index=[0]
    )
    print(new_df["latitude"].item())
    print(type(new_df["latitude"].item()))
    if "eval_button" == ctx.triggered_id:

        table_header = [
            html.Thead(html.Tr([html.Th("Selected Options", style={"font_family": "arial", "color":"#d85e30"}), html.Th("Option Value", style={"font_family": "arial", "color":"#d85e30"})]))
        ]

        row1 = html.Tr([html.Td("Longitude", style={"font-weight": "bold"}), html.Td(longitude_input)])
        row2 = html.Tr([html.Td("Latitude", style={"font-weight": "bold"}), html.Td(latitude_input)])
        row3 = html.Tr([html.Td("Number of Guests", style={"font-weight": "bold"}), html.Td(people_dropdown_eval)])
        row4 = html.Tr([html.Td("Room Type", style={"font-weight": "bold"}), html.Td(roomtype_dropdown_eval)])
        row5 = html.Tr([html.Td("Number of Beds", style={"font-weight": "bold"}), html.Td(num_beds_dropdown_eval)])
        row6 = html.Tr([html.Td("Number of Bathrooms", style={"font-weight": "bold"}), html.Td(num_bathrooms_dropdown_eval)])

        table_body = [html.Tbody([row1, row2, row3, row4, row5, row6])]
        table = dbc.Table(table_header + table_body,
                          bordered=True,
                            # color="primary",
                            hover=True,
                            responsive=True,
                            striped=True)

        pred_val = predict_price(new_df)

        input_guide =  html.Div(dbc.Row([
            dbc.Col([
                html.H5("List of Features", style={"font_family": "arial"}),
                dbc.Alert(["If an input is missing, median value for the particular input is used in making prediction."],
                  id="alert-fade",
                    is_open=True,
                    fade=True,
                    color="warning",
                    style={"fontSize": "14px"}),
            ]),
        ]))

        # input_guide = html.P("Your AirBnB Features:")

        pred_alert = [
        html.P(f"Based on the inputs, your predicted Value per Night is: ${pred_val[0]:.3f} CAD.", style={'fontSize': '15px'})
        ]

        if n_clicks is None:
            fig = create_empty_map(df)
        else:
            fig = create_prediction_map(new_df)

        return pred_alert, table, input_guide, fig
