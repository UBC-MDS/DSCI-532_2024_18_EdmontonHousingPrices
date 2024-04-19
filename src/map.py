import plotly.graph_objects as go
import pandas as pd

def create_map(df_filtered):
    '''Outputs a map with inputs from sidebar'''
    color_bins = [0, 150, 300, 700, 1200]
    color_palette = ['#FED976', '#FD8F3C', '#E3211C', '#7F0F27']
    bin_labels = [f'${color_bins[i]} - ${color_bins[i + 1]}' for i in range(len(color_bins) - 1)]
    
    df_filtered.reset_index(drop=True, inplace=True)
    df_filtered['color'] = pd.cut(df_filtered['price_adjusted'], bins=color_bins, labels=color_palette)
    
    fig = go.Figure()

    # Add map markers
    for i, color in enumerate(color_palette):
        df_color = df_filtered[df_filtered['color'] == color]
        fig.add_trace(go.Scattermapbox(
            lat=df_color["latitude"],
            lon=df_color["longitude"],
            mode="markers",
            text=[f'{df_color["neighbourhood_cleansed"].iloc[j]}<br>' +
                  f'Price/ Night (CAD): ${df_color["price_adjusted"].iloc[j]}<br>' +
                  f'Room Type: {df_color["room_type"].iloc[j]}<br>' +
                  f'Beds: {df_color["beds"].iloc[j]}<br>' +
                  f'Baths: {df_color["bathroom_adjusted"].iloc[j]}<br>' +
                  f'Accommodates: {df_color["accommodates"].iloc[j]}' for j in range(df_color.shape[0])],
            hoverinfo='text',
            marker=dict(
                size=8,
                opacity=0.7,
                color=color,
                showscale=False
            ),
            customdata=df_color,
            name=bin_labels[i]
        ))

    # Update layout
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox_style="carto-positron",
        mapbox_zoom=11,
        mapbox_center={"lat": df_filtered["latitude"].mean(), "lon": df_filtered["longitude"].mean()},
        legend=dict(orientation="h", yanchor="bottom", y=0, xanchor="center", x=0.5, title=None),
        dragmode='select'
    )

    return fig

def create_empty_map(df_filtered):
    '''Creates an empty Vancouver map'''
    df_filtered.reset_index(drop=True, inplace=True)
    
    fig = go.Figure()

    # Add map markers
    fig.add_trace(go.Scattermapbox(
        lat=df_filtered["latitude"],
        lon=df_filtered["longitude"],
        mode="markers",
        marker=dict(
            size=8,
            opacity=0
        ),
        showlegend=False  
    ))

    # Update layout
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox_style="carto-positron",
        mapbox_zoom=11,
        mapbox_center={"lat": df_filtered["latitude"].mean(), "lon": df_filtered["longitude"].mean()},
    )

    return fig


def create_prediction_map(df_filtered, pred_val_string):
    '''Maps one point, based on longitude and latitude inputs'''
    
    fig = go.Figure()

    # Add map marker
    fig.add_trace(go.Scattermapbox(
        lat=df_filtered["latitude"],
        lon=df_filtered["longitude"],
        mode="markers",
        text=["Price / Night (CAD): $" + pred_val_string + '<br>' + 
              "Room Type: " + str(df_filtered["room_type"][i]) + '<br>' +
              "Beds: " + str(df_filtered["beds"][i]) + '<br>' + 
              "Baths: " + str(df_filtered["bathroom_adjusted"][i]) + '<br>' +
              "Accommodates: " + str(df_filtered["accommodates"][i]) for i in range(df_filtered.shape[0])],
        hoverinfo='text',
        marker=dict(
            size=15,
            opacity=1,
            color='#EA5420',
            showscale=False, 
        ),
        showlegend=False  
    ))

    # Update layout
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox_style="carto-positron",
        mapbox_zoom=11,
        mapbox_center={"lat": df_filtered["latitude"].mean(), "lon": df_filtered["longitude"].mean()}
    )

    return fig


