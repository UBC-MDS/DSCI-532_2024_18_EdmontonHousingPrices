import plotly.graph_objects as go

def create_map(df_filtered):
    '''Outputs a map with inputs from sidebar'''
    df_filtered.reset_index(drop=True, inplace=True)
    fig = go.Figure(go.Scattermapbox(
        lat=df_filtered["latitude"],
        lon=df_filtered["longitude"], 
        mode="markers",
        text=[str(df_filtered["neighbourhood_cleansed"][i]) + '<br>' + "Price: $" + str(df_filtered["price_adjusted"][i]) + '<br>' + "Accomodates: " + str(df_filtered["accommodates"][i]) for i in range(df_filtered.shape[0])],
        hoverinfo='text',
        marker=go.scattermapbox.Marker(
            size=df_filtered["accommodates"] * 2,
            sizemin = 4,
            opacity = 0.5,
            color = df_filtered["price_adjusted"],
            showscale=True,
            colorscale='Peach'
        )
        
    ))


    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        mapbox_style="carto-positron",
        mapbox_zoom=11,
        mapbox_center={"lat": df_filtered["latitude"].mean(), "lon": df_filtered["longitude"].mean()}
    )

    return fig