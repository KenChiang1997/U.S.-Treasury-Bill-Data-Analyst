import time 
import numpy as np 
import pandas as pd 
import datetime as dt
from fredapi import Fred 


import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go


dash.register_page(__name__) # Represent Home Page 

layout = html.Div([
    html.Div("Page Still Pending", style={'fontSize':20, 
                                          'margin': '20px'}),
])