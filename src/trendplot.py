import pandas as pd
import plotly.graph_objects as go
from data.real_life_meaning_mapping import real_life_meaning_mapping

# Function to create a time-series plot
def create_aggregated_time_series_plot(df, y_variable=None):
    if y_variable is None:
        y_variable = 'Daily Price'
    y_name = y_variable
    y_variable = real_life_meaning_mapping[y_name]['column_name']
    df = df.copy()
    year_quarter = df['quarter'].str.split('-', expand=True)
    
    # Convert year and quarter into a Period object
    df['quarter'] = pd.PeriodIndex(year=year_quarter[0].astype(int), 
                                   quarter=year_quarter[1].astype(int), 
                                   freq='Q')
    df['quarter'] = df['quarter'].dt.strftime('%Y-Q%q')
    # Aggregating the data
    aggregated_df = df.groupby('quarter')[y_variable].mean().reset_index()
    median_aggregated_df = df.groupby('quarter')[y_variable].median().reset_index()

    # Creating an empty figure and adding both mean and median as separate traces
    fig = go.Figure()

    # Add Mean trace
    fig.add_trace(go.Scatter(x=aggregated_df['quarter'], y=aggregated_df[y_variable],
                             mode='lines', name='Mean'))

    # Adding median trend line
    fig.add_trace(go.Scatter(x=median_aggregated_df['quarter'], y=median_aggregated_df[y_variable],
                             mode='lines', name='Median'))
    # Center the title
    fig.update_layout(
        title={
            'text': f'Trend of the Metric {y_name}',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )
    fig.update_xaxes(title_text='Quarter', tickangle=-45)
    fig.update_yaxes(title_text=f'Average {y_name}')

    fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
            )
    
    fig.update_xaxes(showline=True,
         linewidth=1,
         linecolor='black',
         gridcolor="#E5E4E2",
         mirror=True)
    
    fig.update_yaxes(showline=True,
         linewidth=1,
         linecolor='black',
         gridcolor="#E5E4E2",
         mirror=True,
         title=dict(font=dict(size=13)))
    
    return fig