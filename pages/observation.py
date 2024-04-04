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

# from functions.visualization import map_fig

import plotly.graph_objects as go

import pandas as pd

fig = go.Figure()

dash.register_page(__name__, path="/", title="Observation")

df = pd.read_csv("data/raw/listings.csv")
df = df[df["host_location"] == "Vancouver, Canada"]
df.dropna(subset=['host_location', 'price', 'bathrooms_text'], inplace=True)
df = df[["neighbourhood_cleansed", "accommodates", "price", "room_type", "beds", "bathrooms_text", "quarter"]]

df["price_adjusted"] = df["price"].str.extract(r'([0-9.]+)', expand = False).astype(float)
df["bathroom_adjusted"] = df["bathrooms_text"].str.extract(r'([0-9.]+)', expand = False).astype(float)

SIDEBAR_STYLE = {
    "top": 42,
    "left": 0,
    "bottom": 0,
    "background-color": "#f8f9fa",
    "overflowY": "auto",
}

ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)

sidebar = html.Div([
        html.H4("Apply Filter", style={"margin-left": "14px"}),
        html.Hr(),
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.Label("Select Periods:", style={"color": "black"}),
                    dcc.Checklist(df["quarter"].unique().tolist(),
                                  df["quarter"].unique().tolist(), 
                                  style={"margin-bottom": "15px", "padding-left": 5},
                                  id="quarter_checklist")
                ])
            ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Select Neighbourhood:", style={"color": "black"}),
                          dcc.Dropdown(id="neighbourhood_dropdown",
                                       options=[{"label": r, "value": r} for r in df["neighbourhood_cleansed"].unique().tolist()],
                                       multi=False,
                                       style={"margin-bottom": "20px"})
                    ])
              ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Number of Guests:", style={"color": "black"}),
                          dcc.Dropdown(id="people_dropdown",
                                       options=np.arange(start=1, stop=10, step=1).tolist(),
                                       multi=False,
                                       style={"margin-bottom": "20px"})
                    ])
              ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Room Type:", style={"color": "black"}),
                          dcc.Dropdown(id="roomtype_dropdown",
                                       options=[{"label": r, "value": r} for r in df["room_type"].unique().tolist()],
                                       multi=False,
                                       style={"margin-bottom": "20px"})
                    ])
              ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Price Range (CAD):", style={"color": "black"}),
                          dcc.RangeSlider(min(df["price_adjusted"]), 
                                          max(df["price_adjusted"]), 
                                          10, 
                                          value=[0, df["price_adjusted"].mean()], 
                                          id='price_slider',
                                          marks={
                                            100: {'label': "$100"},
                                            300: {'label': '$300'},
                                            500: {'label': '$500'},
                                            700: {'label': '$700'},
                                            900: {'label': '$900'}, 
                                            
                                        })
                    ])
              ], style={"margin-bottom": "20px"}),

              dbc.Row([
                    dbc.Col([
                          html.Label("Number of Beds:", style={"color": "black"}),
                          dcc.Dropdown(id="num_beds_dropdown",
                                       options=np.arange(start=1, stop=10, step=1).tolist(),
                                       multi=False,
                                       style={"margin-bottom": "20px"})
                    ])
              ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Number of Bathrooms:", style={"color": "black"}),
                          dcc.Dropdown(id="num_bathrooms_dropdown",
                                       options=np.arange(start=0.5, stop=6, step=0.5).tolist(),
                                       multi=False,
                                       style={"margin-bottom": "20px"})
                    ])
              ])

        ])
])

tab1_content = dbc.Card(
    dbc.CardBody(
        dbc.Row([
            dbc.Col([
                dash_table.DataTable(
                        style_table={'overflowX': 'auto'},
                        id="filtered_df",
                        data=df.to_dict("records"),
                        columns=[{'id': c, 'name': c} for c in df.columns],
                        page_size=10,
                        style_cell_conditional=[
                            {
                                'if': {'column_id': c},
                                'textAlign': 'left'
                            } for c in ['Date', 'Region']
                        ],
                        style_as_list_view=True,
                        editable=True,
                        sort_action="native",
                        style_header={"backgroundColor": "#d85e30",
                                      "fontweight": "bold", "color": "black",
                                      "font_size": "14px"},
                        style_cell={"font_family": "arial",
                                    "font_size": "12px",
                                    "text_align": "left"},
                        style_data={'backgroundColor': 'transparent'},
                        sort_mode="single")
            ])
        ])
    ), style={"margin-top":"10px"}
)

tab2_content = dbc.Card(
    dbc.CardBody(
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=fig)
            ])
        ])
    ), className="mt-3"
)


maindiv = html.Div(
    id="first-div",
    children=[
        html.Div([
            html.H4("Available Listings"),
        html.Hr(),
        dbc.Card([
        dbc.CardHeader(
            dbc.Tabs([
                dbc.Tab(tab1_content, label="View as List", tab_style={"marginLeft": "8px",
                                                                       "marginBottom": "10px"}),
                dbc.Tab(tab2_content, label="View in Map", tab_style={"marginRight": "20px"})
                ])
        ),
        ], className="mt-3",
        style={"margin-left": "20px",
               "margin-right": "20px",
               "margin-bottom": "30px",
               "width":"auto"}),
        ]),

        html.Div([
            html.H4("Summary Statistics"),
            html.Hr(),
            html.P(
                dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(dbc.Card(id='avg_accom'))),
                dbc.Col(html.Div(dbc.Card(id='avg_accom'))),
                dbc.Col(html.Div(dbc.Card(id='avg_accom'))),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(dbc.Card(id='avg_accom'))),
                dbc.Col(html.Div(dbc.Card(id='avg_accom'))),
                dbc.Col(html.Div(dbc.Card(id='avg_accom'))),
            ]
        ),
    ]
)
            )
        ], style={"margin-bottom": "30px",
                  "width":"auto"})

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
    [Output("filtered_df", "data"),
    Output("avg_accom", "children")],
    [Input("neighbourhood_dropdown", "value"),
     Input("people_dropdown", "value"),
     Input("price_slider", "value"),
     Input("roomtype_dropdown", "value"),
     Input("num_beds_dropdown", "value"),
     Input("num_bathrooms_dropdown", "value"),
     Input("quarter_checklist", "value")
     ],
     prevent_intial_call=True)
def get_location(neighbourhood_dropdown, 
                 people_dropdown, 
                 price_slider, 
                 roomtype_dropdown, 
                 num_beds_dropdown, 
                 num_bathrooms_dropdown,
                 quarter_checklist):
    
    if quarter_checklist != None:
        df_filtered = df[df["quarter"].isin(quarter_checklist)]

    if quarter_checklist == None:
        df_filtered = df.copy()

    # Filter for neighbourhood
    if neighbourhood_dropdown != None:
        df_filtered = df_filtered[df_filtered["neighbourhood_cleansed"] == neighbourhood_dropdown]

    # Filter for number of people
    if people_dropdown != None:
        df_filtered = df_filtered[df_filtered["accommodates"] == int(people_dropdown)]

    # Filter for price
    if price_slider != None:
        df_filtered = df_filtered[(df_filtered["price_adjusted"] >= int(price_slider[0])) & (df_filtered["price_adjusted"] <= int(price_slider[1]))]

    # Filter for roomtype
    if roomtype_dropdown != None:
        df_filtered = df_filtered[df_filtered["room_type"] == roomtype_dropdown]

    # Filter for number of rooms
    if num_beds_dropdown != None:
        df_filtered = df_filtered[df_filtered["beds"] == num_beds_dropdown]

    # Filter for number of rooms
    if num_bathrooms_dropdown != None:
        df_filtered = df_filtered[df_filtered["bathroom_adjusted"] == num_bathrooms_dropdown]
    
    avg_accom = [
        dbc.CardHeader('Average number of people'),
        dbc.CardBody(f'{df_filtered["accommodates"].mean() :.1f}')
    ]

    return df_filtered.to_dict("records"), avg_accom
