import sys
sys.path.append('../')

from dash import html
import dash_bootstrap_components as dbc
import menu
import dash

dash.register_page(__name__, path="/", title="Observation")

SIDEBAR_STYLE = {
    "top": 42,
    "left": 0,
    "bottom": 0,
    "background-color": "#f8f9fa",
    "overflowY": "auto",
}

sidebar = html.Div(
    [
        html.H3("Filter by:"),
        html.Hr(),
        html.P(
            "Dropdowns go here"
        ),
        # content
    ],
    style=SIDEBAR_STYLE,
)


maindiv = html.Div(
    id="first-div",
    children=[
        html.H1("Observation", style={"color": "#89CFF0",
                                "margin-bottom": "10px"}),
        # first row
        html.Div([
            html.H2("Map"),
            html.Hr(),
            html.P(
                "This is where the map goes", className="lead"
            )
        ]),

        # second row
        html.Div([
            html.H2("Summary Statistics"),
            html.Hr(),
            html.P(
                "This is where summary statistics go", className="lead"
            )
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
