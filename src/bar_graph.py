import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_parquet("data/processed/listings.parquet")

temporary_fig = make_subplots(rows=1, cols=2)

categorical_variables = ["neighbourhood_cleansed", "room_type"]

def create_bar_graph(df):
      fig = make_subplots(rows=2, cols=2, subplot_titles=("Neighbourhood by Count", 
                                                          "Room Type by Count",
                                                          "Number of Available Beds by Count",
                                                          "Number of Available Baths by Count"),
                                                          vertical_spacing = 0.37)

      neighbourhood_df = pd.DataFrame(df["neighbourhood_cleansed"].value_counts())
      room_df = pd.DataFrame(df["room_type"].value_counts())
      bed_df = pd.DataFrame(df["beds"].value_counts())
      baths_df = pd.DataFrame(df["bathroom_adjusted"].value_counts())
      fig.append_trace(
            go.Bar(name="Neighbourhood", x=neighbourhood_df.index, y=neighbourhood_df["count"], showlegend=False),
            row=1, col=1
      )
      fig.append_trace(
            go.Bar(name="Room Type", x=room_df.index, y=room_df["count"], showlegend=False),
            row=1, col=2
      )
      fig.append_trace(
            go.Bar(name="Beds", x=bed_df.index, y=bed_df["count"], showlegend=False),
            row=2, col=1
      )
      fig.append_trace(
            go.Bar(name="Bathrooms", x=baths_df.index, y=baths_df["count"], showlegend=False),
            row=2, col=2
      )

      fig.update_xaxes(row=1, col=1, tickangle=45)
      fig.update_xaxes(row=2, col=1, tickmode='linear')
      fig.update_xaxes(row=2, col=2, tickmode='linear')

      fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
            )
      
      fig.update_layout(
      margin=dict(l=50, r=50, t=20, b=20))  

      fig.update_xaxes(showline=True,
         linewidth=1,
         linecolor='black',
         mirror=True)

      fig.update_yaxes(showline=True,
         linewidth=1,
         linecolor='black',
         mirror=True,
         title=dict(font=dict(size=13)))
      
      return fig

