import plotly.graph_objects as go

def create_map(df_filtered):
    fig = go.Figure(go.Scattermapbox(
        lat=df_filtered["latitude"],
        lon=df_filtered["longitude"], 
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=10,
            opacity = 0.7,
            color = df_filtered["price_adjusted"],
            showscale=True,
            colorscale='Peach'
        )
      #  text=[df_filtered["price_adjusted"], df_filtered["beds"]],
      #  hoverinfo='text'
        
    ))

   # fig.update_traces(hovertemplate='Price: %{price_adjusted} <br>Accomodates: %{accommodates}')

    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        mapbox_style="carto-positron",
        mapbox_zoom=10,
        mapbox_center={"lat": df_filtered["latitude"].mean(), "lon": df_filtered["longitude"].mean()}
    )

    return fig

