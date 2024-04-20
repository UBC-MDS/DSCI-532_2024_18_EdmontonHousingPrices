import sys
sys.path.append('../')

from dash import html
import dash_bootstrap_components as dbc
import menu
import dash
from dash import dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app import app
from app import cache
from dash import Dash, html, dcc, dash_table, ctx
from dash import callback_context
import numpy as np
from data.real_life_meaning_mapping import real_life_meaning_mapping
import plotly.graph_objects as go
from src.trendplot import create_aggregated_time_series_plot
# import dash_vega_components as dvc
# from functions.visualization import map_fig

import plotly.graph_objects as go
import plotly.express as px

from src.bar_graph import temporary_fig, create_bar_graph

import pandas as pd
from src.map import create_map, create_empty_map

dash.register_page(__name__, path="/", title="Observation")

df = pd.read_parquet("data/processed/listings.parquet") ### This is the processed version of our data sufficent for all functionalities

simulated = pd.read_parquet('data/processed/simulated.parquet') ### This is the simulated data for the trend section

default_guests = round(df["accommodates"].mean(), 2)
default_price = round(df["price_adjusted"].mean(), 2)
default_beds = round(df["beds"].mean(), 2)
default_baths = round(df["bathroom_adjusted"].mean(), 2)

### This is a special column-selected version for list visualization but not exhaustive for other plotting functions
# so we do not store this data directly as processed data
df_cleaned = df[["quarter", "neighbourhood_cleansed", "accommodates", "price", "room_type", "beds", "bathrooms_text"]]
df_cleaned.columns = ["Quarter", "Neighbourhood", "Number of Guests", "Price (CAD)", "Room Type", "Available Beds", "Available Bathrooms"]

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

reset_button = html.Button('Reset the Map Selection', id='reset_button', n_clicks=0)

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
                                       multi=True,
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
                                       multi=True,
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
                                       multi=True,
                                       style={"margin-bottom": "20px"})
                    ])
              ]),

              dbc.Row([
                    dbc.Col([
                          html.Label("Number of Bathrooms:", style={"color": "black"}),
                          dcc.Dropdown(id="num_bathrooms_dropdown",
                                       options=np.arange(start=0.5, stop=6, step=0.5).tolist(),
                                       multi=True,
                                       style={"margin-bottom": "20px"})
                    ])
              ])

        ])
], style={
    'position': 'sticky',
    'top': '20px',  # Adjust this value based on your header's height or navbar if present
    'height': 'calc(100vh - 40px)',  # Adjust the height calculation based on your layout needs
    'overflow-y': 'auto'
    })

tab1_content = dbc.Card(
    dbc.CardBody(
        dbc.Row([
            dbc.Col([
                dash_table.DataTable(
                        style_table={'overflowX': 'auto'},
                        id="filtered_df",
                        data=df_cleaned.to_dict("records"),
                        columns=[{'id': c, 'name': c} for c in df_cleaned.columns],
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
                        style_header={"backgroundColor": "#F1F1F1",
                                      "fontWeight": "bold",
                                      "font_family": "arial",
                                      "color": "#d85e30",
                                      "text_align":"center",
                                      "font_size": "14px"},
                        style_cell={"font_family": "arial",
                                    "font_size": "13px",
                                    'padding': '5px',
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
                dcc.Graph(id = "map",
                          figure=create_map(df))
            ])
        ])
    ), className="mt-3"
)

tab3_content = dbc.Card(
    dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dcc.RadioItems(['Mean', 'Median'], 'Mean', inline=True, id="average_radio", style={"margin-bottom":"20px", "margin-left":"10px"}), 
                dbc.CardGroup([
                    dbc.Card([
                        dbc.CardHeader('Number of Guests', style={"text-align": "center", "color": "#d85e30"}),
                        dbc.CardBody(html.P(default_guests, id="avg_guests", style={"text-align": "center", "fontSize":16, "fontWeight": "bold",}))
                    ], color='primary', outline=True),
                    dbc.Card([
                        dbc.CardHeader('Price per Night (CAD)', style={"text-align": "center", "color": "#d85e30",}),
                        dbc.CardBody(html.P(default_price, id="avg_price", style={"text-align": "center", "fontSize":16, "fontWeight": "bold",}))
                    ], color='primary', outline=True),
                    dbc.Card([
                        dbc.CardHeader('Number of Beds', style={"text-align": "center", "color": "#d85e30",}),
                        dbc.CardBody(html.P(default_beds, id="avg_beds", style={"text-align": "center", "fontSize":16, "fontWeight": "bold",}))
                    ], color='primary', outline=True),
                    dbc.Card([
                        dbc.CardHeader('Number of Baths', style={"text-align": "center", "color": "#d85e30"}),
                        dbc.CardBody(html.P(default_baths,id="avg_baths", style={"text-align": "center", "fontSize":16, "fontWeight": "bold",}))
                    ], color='primary', outline=True),
                ], style={"margin-bottom": "20px"})
            ]),
        ]),
    ]),
    className="mt-3", 
)

tab4_content = dbc.Card([
    dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dcc.Graph(id="histograms_fig", figure=create_bar_graph(df))
            ])
        ])
    ], style={"margin-top":"10px", "margin-left":"10px"})
], style={"margin-top":"10px"})

maindiv = html.Div(
    id="first-div",
    children=[
        html.Div([
            html.H4("Available Listings"),
        html.Hr(),
        dbc.Card([
        dbc.CardHeader(
            dbc.Tabs([
                dbc.Tab(tab2_content, label="View in Map", tab_style={"marginLeft": "8px",
                                                                       "marginBottom": "10px"}),
                dbc.Tab(tab1_content, label="View as List", tab_style={"marginRight": "20px"})
                ], active_tab="tab-0")
        ),
        html.Div([
            dbc.Button("Reset Map Selection", id="reset_button", color="secondary", className="mb-3", style={'background-color': '#E8582E',"width": "15%"})  # Adding reset button below the tabs
        ], style={'display': 'flex', 'justifyContent': 'flex-end'})
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
                dbc.Container([

        dbc.Card([dbc.CardHeader(
            dbc.Tabs([
                dbc.Tab(tab4_content, label="Categorical Data", tab_style={"margin-left":"0px"}),
                dbc.Tab(tab3_content, label="Numerical Data", tab_style={"margin-bottom": "10px"})
                ], active_tab="tab-0")
        ),
        ], style={"margin-left":"10px"})
    ],
)
            )
        ], style={"margin-bottom": "30px",
                  "margin-right":"10px",
                  "width":"auto"}),

        html.Div([
            html.H4("Trends of Key Metrics Over Time"),
            html.Hr(),
            dbc.Alert([
                        "Please note that this part is based on simulated data extending to the previous quarters, as the complete dataset is still being requested. ",
                        html.Br(),
                        "To understand the logic of the simulation, please see the time series exploration with ",
                        html.A("the notebook", 
                            href="https://github.com/UBC-MDS/DSCI-532_2024_18_VancouverAirbnbPrices/blob/main/notebooks/data_exploration_time_series.ipynb"),
                        "."
                        ],
                style={'fontSize': '13px', "margin-left": "8px", "margin-right":"9px"},
                dismissable=True,
                    is_open=True,
                    fade=True,
                    color="warning",),
            # html.P([
            #     "Please note that this part is based on simulated data extending to the previous quarters, as the complete dataset is still being requested. ",
            #     html.Br(),
            #     "To understand the logic of the simulation, please see notebooks/data_exploration_time_series.ipynb."],
            #     style={'fontSize': '13px'}),  # Adjust the font size as needed,
            
            html.Label("Select one metric for Plotting the Trend:", style={"color": "black"}),
            dcc.Dropdown(id="metrics_dropdown",
                        options=[{'label': key, 'value': key} for key in real_life_meaning_mapping.keys()],
                        multi=False,
                        style={"margin-bottom": "20px", "margin-right": "20px"}),
            # Add a Div to display the description of the selected metric
            html.Div(id='metric-description', children='Description of the metric will be shown after selection!',style={"color": "black", "margin-bottom": "20px", "margin-right": "30px"}),
            dcc.Graph(
                id='metric-time-series',
                figure=create_aggregated_time_series_plot(
                    simulated[(simulated["price"] >= 0) & (simulated["price"] <= int(df["price_adjusted"].mean()))])
                )
        ], style={"margin-bottom": "30px",
                  "width":"auto", 
                  })

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
    Output("map", "figure"),
    Output("avg_guests", "children"),
    Output("avg_price", "children"),
    Output("avg_beds", "children"),
    Output("avg_baths", "children"),
    Output("histograms_fig", "figure")],
    [Input("neighbourhood_dropdown", "value"),
     Input("people_dropdown", "value"),
     Input("price_slider", "value"),
     Input("roomtype_dropdown", "value"),
     Input("num_beds_dropdown", "value"),
     Input("num_bathrooms_dropdown", "value"),
     Input("quarter_checklist", "value"),
     Input("map", "selectedData"),
     Input("average_radio", "value"),
     Input("reset_button", "n_clicks") # add this line to keep track of the previous selection
     ],  
     prevent_intial_call=True)
@cache.memoize()
def get_location(neighbourhood_dropdown, 
                 people_dropdown, 
                 price_slider, 
                 roomtype_dropdown, 
                 num_beds_dropdown, 
                 num_bathrooms_dropdown,
                 quarter_checklist,
                 selectedData,
                 average_radio,
                 reset_clicks):
    
    df_filtered = df.copy()

    # Check if filters are modified or if a fresh map selection is made
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Reset functionality
    if input_id != "reset_button": # only narrowing down to selected area when it is not reset
        if selectedData:
            selected_data = pd.DataFrame([point['customdata'] for point in selectedData['points']])
            selected_data.columns = df.columns
            df_filtered = selected_data

    # but we would honor the sidebar filters no matter we reset or honor the selected area
    # Apply other filters
    if quarter_checklist is not None and len(quarter_checklist)>0:
        df_filtered = df_filtered[df_filtered["quarter"].isin(quarter_checklist)]

    # if quarter_checklist is None:
    #     df_filtered = df_filtered.copy()

    # Filter for neighbourhood
    if neighbourhood_dropdown != None and len(neighbourhood_dropdown)>0:
        df_filtered = df_filtered[df_filtered["neighbourhood_cleansed"].isin(neighbourhood_dropdown)]

    # Filter for number of people
    if people_dropdown != None:
        df_filtered = df_filtered[df_filtered["accommodates"] == int(people_dropdown)]

    # Filter for price
    if price_slider != None:
        df_filtered = df_filtered[(df_filtered["price_adjusted"] >= int(price_slider[0])) & (df_filtered["price_adjusted"] <= int(price_slider[1]))]

    # Filter for roomtype
    if roomtype_dropdown != None and len(roomtype_dropdown)>0:
        df_filtered = df_filtered[df_filtered["room_type"].isin(roomtype_dropdown)]

    # Filter for number of rooms
    if num_beds_dropdown != None and len(num_beds_dropdown)>0:
        df_filtered = df_filtered[df_filtered["beds"].isin(num_beds_dropdown)]

    # Filter for number of rooms
    if num_bathrooms_dropdown != None and len(num_bathrooms_dropdown)>0:
        df_filtered = df_filtered[df_filtered["bathroom_adjusted"].isin(num_bathrooms_dropdown)]

    if len(df_filtered) > 0:
        fig = create_map(df_filtered)
        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox_zoom=10,
            mapbox_center={"lat": df_filtered["latitude"].mean(), "lon": df_filtered["longitude"].mean()}
        )
    
    elif len(df_filtered) == 0: 
        fig = create_empty_map(df)

    avg_accom = [
        dbc.CardHeader('Average Number of Accomodates (Guests)', style={"text-align": "center"}),
        dbc.CardBody(f'{df_filtered["accommodates"].mean() :.1f}', style={"text-align": "center"})
    ]

    if average_radio == "Mean":
        avg_guest = round(df_filtered["accommodates"].mean(), 2)
        avg_price = round(df_filtered["price_adjusted"].mean(), 2)
        avg_beds = round(df_filtered["beds"].mean(), 2)
        avg_baths = round(df_filtered["bathroom_adjusted"].mean(), 2)
    elif average_radio == "Median":
        avg_guest = round(df_filtered["accommodates"].median(), 3)
        avg_price = round(df_filtered["price_adjusted"].median(), 3)
        avg_beds = round(df_filtered["beds"].median(), 3)
        avg_baths = round(df_filtered["bathroom_adjusted"].median(), 3)

    bar_fig = create_bar_graph(df_filtered)

    df_cleaned = df_filtered.copy()
    df_cleaned = df_filtered[["quarter", "neighbourhood_cleansed", "accommodates", "price", "room_type", "beds", "bathrooms_text"]]
    df_cleaned.columns = ["Quarter", "Neighbourhood", "Number of Guests", "Price (CAD)", "Room Type", "Available Beds", "Available Bathrooms"]

    return df_cleaned.to_dict("records"), fig,  avg_guest, avg_price, avg_beds, avg_baths, bar_fig


@app.callback(
    Output('metric-time-series', 'figure'),
    [Input("neighbourhood_dropdown", "value"),
     Input("people_dropdown", "value"),
     Input("price_slider", "value"),
     Input("roomtype_dropdown", "value"),
     Input("num_beds_dropdown", "value"),
     Input("num_bathrooms_dropdown", "value"),
     Input("metrics_dropdown", "value"),
     Input("map", "selectedData"),
     Input("reset_button", "n_clicks")
     ],
     prevent_intial_call=True)
@cache.memoize()
def create_plot(neighbourhood_dropdown, 
                 people_dropdown, 
                 price_slider, 
                 roomtype_dropdown, 
                 num_beds_dropdown, 
                 num_bathrooms_dropdown,
                 metrics_dropdown,
                 selectedData,
                 reset_clicks):
    

    filtered_simulated = simulated.copy() 

    # Select metric
    if metrics_dropdown != None:
        metric_string = metrics_dropdown
    else:
        metric_string = None

    # Check if filters are modified or if a fresh map selection is made
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Reset functionality
    if input_id != "reset_button": # only narrowing down to selected area when it is not reset
        if selectedData is not None:
            # details = [point['text'] for point in points]
            selected_data = pd.DataFrame([point['customdata'] for point in selectedData['points']])
            selected_data.columns = df.columns
            lst_neighborhood = selected_data['neighbourhood_cleansed'].unique().tolist()
            filtered_simulated = filtered_simulated[filtered_simulated['neighbourhood'].transform(lambda x: x in lst_neighborhood)]
            # return create_aggregated_time_series_plot(filtered_simulated, metric_string)

    # other global filtering conditions in the sidebar
    # Filter for neighbourhood
    if neighbourhood_dropdown != None and len(neighbourhood_dropdown)>0:
        filtered_simulated = filtered_simulated[filtered_simulated["neighbourhood"].isin(neighbourhood_dropdown)]

    # Filter for number of people
    if people_dropdown != None:
        filtered_simulated = filtered_simulated[filtered_simulated["number_of_guests"] == int(people_dropdown)]
    # Filter for price
    if price_slider != None:
        filtered_simulated = filtered_simulated[(filtered_simulated["price"] >= int(price_slider[0])) & (filtered_simulated["price"] <= int(price_slider[1]))]
    # Filter for roomtype
    if roomtype_dropdown != None and len(roomtype_dropdown)>0:
        filtered_simulated = filtered_simulated[filtered_simulated["room_type"].isin(roomtype_dropdown)]
    # Filter for number of rooms
    if num_beds_dropdown != None and len(num_beds_dropdown)>0:
        filtered_simulated = filtered_simulated[filtered_simulated["number_of_beds"].isin(num_beds_dropdown)]

    # Filter for number of rooms
    if num_bathrooms_dropdown != None and len(num_bathrooms_dropdown)>0:
        filtered_simulated = filtered_simulated[filtered_simulated["number_of_bathrooms"].isin(num_bathrooms_dropdown)]

    # Check if the filtered data is empty
    if filtered_simulated.empty:
        # Return a figure with a message indicating no data
        return {
            'data': [],
            'layout': go.Layout(
                title='No data available for the selected filters.',
                xaxis={'visible': False},
                yaxis={'visible': False},
                annotations=[{
                    'text': 'No data available',
                    'xref': 'paper',
                    'yref': 'paper',
                    'showarrow': False,
                    'font': {'size': 28}
                }]
            )
        }

    return create_aggregated_time_series_plot(filtered_simulated, metric_string)

@app.callback(
    Output('metric-description', 'children'),
    [Input('metrics_dropdown', 'value')]
)
@cache.memoize()
def update_description(selected_metric):
    description = real_life_meaning_mapping[selected_metric]['description']
    return description
