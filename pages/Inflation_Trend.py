import time 
import numpy as np 
import pandas as pd 
import datetime as dt

from fredapi import Fred 
from Utils.inflation_module import get_inflation_dataset, get_detail_commodity_data, get_organized_cpi_data, get_pce_data, get_organized_pce_data
from Utils.inflation_visualization import plot_inflation_data, plot_detail_commodity_data, plot_cpi_annualized_tend, plot_pce_cpi_indicator_chart, plot_inflation_indicator_chart

import dash
from dash import dcc, html, dash_table



dash.register_page(__name__, path = "/") # Represent Home Page 

# -------------- Page 1 Data -------------

api_key = 'a0aee094a9b908bd7c16baece8df8419'
fred = Fred(api_key = 'a0aee094a9b908bd7c16baece8df8419')

inflation_data = get_inflation_dataset(fred)
detail_commodity_data, wti_crude_oil = get_detail_commodity_data(fred)
pce_data = get_pce_data(fred, inflation_data)


organized_cpi_data = get_organized_cpi_data(inflation_data)
organized_pce_data = get_organized_pce_data(pce_data)

inflation_plot = plot_inflation_data(inflation_data.tail(50))
inflation_mom_plot = plot_cpi_annualized_tend(inflation_data.tail(20))
detail_inflation_plot = plot_detail_commodity_data(wti_crude_oil.tail(100), detail_commodity_data.tail(30))
pce_indicator_plot = plot_pce_cpi_indicator_chart(pce_data.tail(80))
volatility_indicator_plot = plot_inflation_indicator_chart(fred, pce_data.tail(300))


# ------------------------------------------

layout = html.Div([
        # Heder Setting
        html.Div([html.H1(children = "Inflation Trend Breakdown Analysis, Data Source: FRED - Federal Reserve Economic Data", 
                          style = {'textAlign': 'center', 'font-size': '25px', 'text-align': 'left'})]),
                
        html.Div(children = [
                          html.P(children = "1.) Consumer Price Index Trend - Overall Market", 
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
                          
                          html.Div(children = [ dcc.Graph(id = "inflation_chart",  figure = inflation_plot),
                                                dash_table.DataTable(data = organized_cpi_data.reset_index().to_dict('records'), 
                                                                      style_cell = {'textAlign': 'right'},
                                                                      style_cell_conditional = [{'if': {'column_id': 'open_time'},'textAlign': 'left'}],
                                                                      style_header = {'backgroundColor': '#2c5c97', 'fontWeight': 'bold', 'color':'#D1D9DB', 'font-size': '18px', 'textAlign': 'center'},
                                                                      style_data = {'backgroundColor': 'White', "whiteSpace": 'auto', "height":"auto", 'textAlign': 'center', 'font-size': '15px'},
                                                                      style_table = {'width': '1250px', 'overflowY': 'auto', 'margin-top': '10px', 'margin-left' : '20px'}, ), ]),

                          html.P(children = "1.1) Inflation Trend MoM - Overall Market",
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
                                  
                          dcc.Graph(id = "Inflation_MoM_Chart", figure = inflation_mom_plot, style = {'margin-left' : '10px' }),

                          html.P(children = "1.2) Detail Commodity Inflation Trend", id = 'output-data-upload', 
                                    style = {'font-size': '20px', 
                                            'width': '50%', 
                                            'border-radius': '20px', 
                                            'text-align': 'left', 
                                            "padding-left": "20px", 
                                            'font-family' : 'Roboto', 
                                            "margin-left" : "20px", 
                                            "margin-up" : "-120px", 
                                            'background' : 'rgb(233 238 246)'}),

                          dcc.Graph(id = "Detail_Inflation_Chart", figure = detail_inflation_plot, style = {'margin-left' : '10px' }),

                          html.P(children = "1.3) Personal Consumption Expenditures Price Index", id = 'output-data-upload', 
                                    style = {'font-size': '20px', 
                                            'width': '50%', 
                                            'border-radius': '20px', 
                                            'text-align': 'left', 
                                            "padding-left": "20px", 
                                            'font-family' : 'Roboto', 
                                            "margin-left" : "20px", 
                                            "margin-up" : "-120px", 
                                            'background' : 'rgb(233 238 246)'}),

                          dcc.Graph(id = "Detail_PCE_Chart", figure = pce_indicator_plot, style = {'margin-left' : '10px' }),
                          dash_table.DataTable(data = organized_pce_data.reset_index().to_dict('records'), 
                                                                      style_cell = {'textAlign': 'right'},
                                                                      style_cell_conditional = [{'if': {'column_id': 'open_time'},'textAlign': 'left'}],
                                                                      style_header = {'backgroundColor': '#2c5c97', 'fontWeight': 'bold', 'color':'#D1D9DB', 'font-size': '18px', 'textAlign': 'center'},
                                                                      style_data = {'backgroundColor': 'White', "whiteSpace": 'auto', "height":"auto", 'textAlign': 'center', 'font-size': '15px'},
                                                                      style_table = {'width': '1200px', 'overflowY': 'auto', 'margin-top': '-5px', 'margin-left' : '20px', 'margin-bottom' : '20px'}),


                          html.P(children = "1.4) Inflation Difference Volatility Indicator", id = 'output-data-upload', 
                                    style = {'font-size': '20px', 
                                            'width': '50%', 
                                            'border-radius': '20px', 
                                            'text-align': 'left', 
                                            "padding-left": "20px", 
                                            'font-family' : 'Roboto', 
                                            "margin-left" : "20px", 
                                            "margin-up" : "-120px", 
                                            'background' : 'rgb(233 238 246)'}),

                          dcc.Graph(id = "Indicator_Chart", figure = volatility_indicator_plot, style = {'margin-left' : '10px' }),

                          ],  style = {'display': 'flex', 'flexDirection': 'column', 'gap': '35px'})

])
