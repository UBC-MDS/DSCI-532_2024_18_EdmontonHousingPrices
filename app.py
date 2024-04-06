import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, ctx
import pandas as pd

df = pd.read_csv("data/raw/listings.csv")

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.UNITED, dbc.icons.BOOTSTRAP],
                title="Vancouver AirBnB Listings",
                pages_folder="pages",
                suppress_callback_exceptions=True,
                prevent_initial_callbacks=True)

