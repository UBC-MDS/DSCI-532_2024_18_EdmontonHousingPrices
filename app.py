import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, ctx

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP],
                title="Vancouver AirBnB Listings",
                pages_folder="pages",
                suppress_callback_exceptions=True)

server = app.server