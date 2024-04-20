from dash import html
from dash import dcc
from dash.dependencies import Input, Output

from app import app
from app import cache
from pages import observation, prediction, credentials

url_content_layout = html.Div(children=[
    dcc.Location(id="url",refresh=False),
    html.Div(id="output-div")
])

server = app.server

app.layout = url_content_layout

app.validation_layout = html.Div([
    url_content_layout,
    observation.layout
])

@app.callback(
    Output(component_id="output-div",component_property="children"),
    Input(component_id="url",component_property="pathname"))
@cache.memoize()
def update_output_div(pathname):
    if pathname == "/":
        return observation.layout
    elif pathname == "/prediction":
        return prediction.layout
    elif pathname == "/credentials":
        return credentials.layout

if __name__ == "__main__":
    app.run(debug=True, port=4444)