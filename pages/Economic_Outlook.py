import time 
import numpy as np 
import pandas as pd 
import datetime as dt

from fredapi import Fred 
from Utils.economic_module import get_economic_outlook_data, get_us_gdp_data
from Utils.economic_visualization import plot_real_wage_and_salary, plot_inventory_spread, plot_consumer_confidence, plot_us_gdp_data

import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go


dash.register_page(__name__) # Represent Home Page 

api_key = 'a0aee094a9b908bd7c16baece8df8419'
fred = Fred(api_key = 'a0aee094a9b908bd7c16baece8df8419')

economic_outlook_data = get_economic_outlook_data(fred)
gdp_df = get_us_gdp_data(fred)

real_wage_chart = plot_real_wage_and_salary(economic_outlook_data)
inventory_spread_chart = plot_inventory_spread(economic_outlook_data)
consumer_confidence_chart = plot_consumer_confidence(economic_outlook_data)
us_gdp_chart = plot_us_gdp_data(gdp_df)


layout = html.Div([

        # Heder Setting
        html.Div([html.H1(children = "Economic Trend Overview, Data Source: FRED - Federal Reserve Economic Data", 
                          style = {'textAlign': 'center', 'font-size': '25px', 'text-align': 'left', 'margin-left' : '10px'})]),

        html.P(children = "1.1) Overall Consumer Purchase Ability",
                id = 'output-data-upload', 
                style = {'font-size': '20px', 
                    'width': '50%', 
                    'border-radius': '20px', 
                    'text-align': 'left', 
                    "padding-left": "20px", 
                    'font-family' : 'Roboto', 
                    "margin-left" : "20px", 
                    "margin-up" : "-120px", 
                    'background' : 'rgb(233 238 246)'}),
                                  
        dcc.Graph(id = "Real_Wage_Chart", figure = real_wage_chart, style = {'margin-left' : '10px' }),

        html.P(children = "1.2) ISM Manufacture Inventory Dataset",
                id = 'output-data-upload', 
                style = {'font-size': '20px', 
                    'width': '50%', 
                    'border-radius': '20px', 
                    'text-align': 'left', 
                    "padding-left": "20px", 
                    'font-family' : 'Roboto', 
                    "margin-left" : "20px", 
                    "margin-up" : "-120px", 
                    'background' : 'rgb(233 238 246)'}),
                                  
        dcc.Graph(id = "inventory_Spread_Chart", figure = inventory_spread_chart, style = {'margin-left' : '10px' }),

        html.P(children = "1.3) Michigan Consumer Confidence Index",
                id = 'output-data-upload', 
                style = {'font-size': '20px', 
                    'width': '50%', 
                    'border-radius': '20px', 
                    'text-align': 'left', 
                    "padding-left": "20px", 
                    'font-family' : 'Roboto', 
                    "margin-left" : "20px", 
                    "margin-up" : "-120px", 
                    'background' : 'rgb(233 238 246)'}),
                                  
        dcc.Graph(id = "consumer_confidence_chart", figure = consumer_confidence_chart, style = {'margin-left' : '10px' }),

        html.P(children = "1.4) U.S. GDP Data",
                id = 'output-data-upload', 
                style = {'font-size': '20px', 
                    'width': '50%', 
                    'border-radius': '20px', 
                    'text-align': 'left', 
                    "padding-left": "20px", 
                    'font-family' : 'Roboto', 
                    "margin-left" : "20px", 
                    "margin-up" : "-120px", 
                    'background' : 'rgb(233 238 246)'}),
                                  
        dcc.Graph(id = "us_gdp_chart", figure = us_gdp_chart, style = {'margin-left' : '10px' }),

])