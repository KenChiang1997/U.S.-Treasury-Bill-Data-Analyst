import numpy as np 
import pandas as pd 

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
temp = dict(layout = go.Layout(font = dict(family="Franklin Gothic", size=12), width = 1500))

def plot_real_wage_and_salary(economic_outlook_data):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x = economic_outlook_data['index'], 
                y = economic_outlook_data['Real Personal Income(excluding transfer) YoY'], 
                name = 'Real Personal Income(excluding transfer) YoY',
                line = dict(color = 'blue')))

    fig.add_trace(
        go.Scatter(x = economic_outlook_data['index'], 
                y = economic_outlook_data['Real Personal Income Expenditure YoY'], 
                name = 'Real Personal Income Expenditure YoY',
                line = dict(color = 'orange')))

    fig.add_trace(
        go.Bar(x = economic_outlook_data['index'], 
                y = economic_outlook_data['Household Wage & Salary YoY'], 
                name = 'Household Wage & Salary YoY',
                yaxis = 'y2',
                marker = dict(color = 'green')))

    fig.update_layout(title = "Real Personal Income/Expenditure & Household Salary",
                    title_font = dict(size = 15),
                    width = 1200,
                    height = 500,
                    margin = dict(l = 40, r = 40, t = 40, b = 80),
                    annotations = [dict( text = "Data Source: FRED - Federal Reserve Economic Data",
                                    x = 0,
                                    y = - 0.15,
                                    xref = "paper",
                                    yref = "paper",
                                    showarrow = False)],
                                    
                    yaxis2 = dict(title = "Household Salary YoY(%)", overlaying = "y", side = "right"),
                    legend = dict(x = 0, y = 0))

    return fig

def plot_inventory_spread(economic_outlook_data):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x = economic_outlook_data['index'], 
                y = economic_outlook_data['Client Inventory'], 
                name = 'Manufacture Client Inventory',
                line = dict(color = 'navy')))

    fig.add_trace(
        go.Scatter(x = economic_outlook_data['index'], 
                y = economic_outlook_data['Manufacture Inventory'], 
                name = 'Manufacture Inventory',
                line = dict(color = 'brown')))

    fig.add_trace(
        go.Bar(x = economic_outlook_data['index'], 
                y = economic_outlook_data['Inventory Spread'], 
                name = 'Inventory Spread',
                yaxis = 'y2',
                marker = dict(color = 'black')))

    fig.update_layout(title = "ISM - Manufacture Inventory Data, Last update date: " + str(economic_outlook_data['index'].to_list()[-1])[:7] ,
                    title_font = dict(size = 15),
                    width = 1200,
                    height = 500,
                    margin = dict(l = 40, r = 40, t = 40, b = 80),
                    annotations = [dict( text = "Data Source: FRED - Federal Reserve Economic Data",
                                    x = 0,
                                    y = - 0.15,
                                    xref = "paper",
                                    yref = "paper",
                                    showarrow = False)],
                                    
                    yaxis2 = dict(title = "Inventory Spread", overlaying = "y", side = "right"),
                    legend = dict(x = 0, y = 0))

    return fig


def plot_consumer_confidence(economic_outlook_data):

    fig = go.Figure()

    fig.add_trace(
    go.Scatter(x = economic_outlook_data['index'], 
            y = economic_outlook_data['Michigan: Consumer Sentiment'], 
            name = 'Michigan: Consumer Sentiment',
            line = dict(color = 'navy')))
    
    fig.add_trace(
    go.Scatter(x = economic_outlook_data['index'], 
            y = economic_outlook_data['Inventory Spread'], 
            name = 'ISM Inventory Spread',
            yaxis = 'y2',
            line = dict(color = 'black')))
    
    fig.update_layout(title = 'Michigan: Consumer Sentiment & Inventory Spread',
                    title_font = dict(size = 15),
                    width = 1200,
                    height = 500,
                    margin = dict(l = 40, r = 40, t = 40, b = 80),
                    annotations = [dict( text = "Data Source: FRED - Federal Reserve Economic Data",
                                    x = 0,
                                    y = - 0.15,
                                    xref = "paper",
                                    yref = "paper",
                                    showarrow = False)],
                    yaxis2 = dict(title = "Inventory Spread", overlaying = "y", side = "right"),
                    showlegend = True,
                    legend = dict(x = 0, y = 0))
    
    return fig 

def plot_us_gdp_data(gdp_df):

    fig = make_subplots(rows = 1, 
                        cols = 2,
                        subplot_titles = ("U.S. GDP Quarter over Quarter Performance", "U.S. GDP Year over Year Performance"))

    fig.add_trace(
        go.Scatter(x = gdp_df['index'], 
                y = gdp_df['Real GDP QoQ'], 
                name = "Real GDP QoQ",
                line = dict(color = 'blue')), row = 1, col = 1)

    fig.add_trace(
        go.Scatter(x = gdp_df['index'], 
                y = gdp_df['Nominal GDP QoQ'], 
                name = "Nominal GDP QoQ",
                line = dict(color = 'red')), row = 1, col = 1)

    fig.add_trace(
        go.Scatter(x = gdp_df['index'], 
                y = gdp_df['Real GDP YoY'], 
                name = "Real GDP YoY",
                line = dict(color = 'blue', dash = "dash")), row = 1, col = 2)

    fig.add_trace(
        go.Scatter(x = gdp_df['index'], 
                y = gdp_df['Nominal GDP YoY'], 
                name = "Nominal GDP YoY",
                line = dict(color = 'red', dash = "dash")), row = 1, col = 2)

    fig.update_layout(width = 1200,
                    height = 350,
                    margin = dict(l = 40, r = 0, t = 40, b = 30))
    
    return fig