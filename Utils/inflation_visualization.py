import numpy as np 
import pandas as pd 
import datetime as dt

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
temp = dict(layout = go.Layout(font = dict(family="Franklin Gothic", size=12), width = 1500))


def plot_inflation_data(inflation_data):

    latest_release_inflation_data = inflation_data.iloc[-1]

    fig = make_subplots(rows = 1, cols = 3, subplot_titles = ("CPI YoY and Core CPI YoY", "Food and Energy", "Latest Release CPI Data for " + str(inflation_data['index'].to_list()[-1])[:7] ))

    fig.add_trace(
        go.Scatter(x = inflation_data['index'], 
                y = inflation_data['CPI YoY'], 
                name = 'CPI YoY',
                line = dict(color = 'black')),
                row = 1,
                col = 1)

    fig.add_trace(
        go.Scatter(x = inflation_data['index'], 
                y = inflation_data['Core CPI YoY'], 
                name = 'Core CPI YoY',
                line = dict(color = 'green')),
                row = 1,
                col = 1)

    fig.add_trace(
        go.Scatter(x = inflation_data['index'], 
                y = inflation_data['Sticky CPI YoY'], 
                name = 'Sticky CPI YoY',
                line = dict(color = 'red')),
                row = 1,
                col = 1)

    fig.add_trace(
        go.Scatter(x = inflation_data['index'], 
                y = inflation_data['Food CPI YoY'], 
                name = 'Food CPI YoY',
                line = dict(dash = "dash", color = '#119DFF')),
                row = 1,
                col = 2)

    fig.add_trace(
        go.Scatter(x = inflation_data['index'], 
                y = inflation_data['Energy CPI YoY'], 
                name = 'Energy CPI YoY',
                line = dict(dash = "dash", color = 'Navy')),
                row = 1,
                col = 2)

    fig.add_trace(
        go.Bar(x = latest_release_inflation_data[['CPI YoY', 'Core CPI YoY', 'Food CPI YoY', 'Energy CPI YoY']].index,
            y = latest_release_inflation_data[['CPI YoY', 'Core CPI YoY', 'Food CPI YoY', 'Energy CPI YoY']].values,
            marker = dict(color = ['black', 'green', '#119DFF', 'Navy']), 
            text = ['CPI YoY', 'Core CPI YoY', 'Food CPI YoY', 'Energy CPI YoY']), row = 1, col = 3)

    fig.update_layout(template = temp,
                    hovermode = 'closest',
                    margin = dict(l = 20, r = 0, t = 20, b = 50),
                    height = 350, 
                    width = 1300, 
                    xaxis = dict(tickfont = dict(size = 10)),
                    yaxis = dict(side = "left", tickfont = dict(size=10)),
                    yaxis2 = dict(side = "right", overlaying = "y", tickfont = dict(size=10) ))

    return fig 



def plot_detail_commodity_data(wti_crude_oil, detail_commodity_data):

    fig = make_subplots(rows = 1, cols = 3, subplot_titles = ("Crude Oil West Texas Intermediate (WTI)",
                                                            "Used Cars and Trucks in U.S. City Average", 
                                                            "Owners' Equivalent Rent QoQ(%)"))

    fig.add_trace(
        go.Scatter(x = wti_crude_oil['index'], 
                y = wti_crude_oil['Crude Oil West Texas Intermediate (WTI)'], 
                name = 'Crude Oil West Texas Intermediate (WTI)',
                line = dict(color = 'black')),
                row = 1,
                col = 1)

    fig.add_trace(
        go.Scatter(x = detail_commodity_data['index'], 
                y = detail_commodity_data['Used Cars and Trucks in U.S. City Average'],
                name = 'Used Cars and Trucks in U.S. City Average',
                line = dict(color = '#11FFE4')),
                row = 1,
                col = 2)


    fig.add_trace(
        go.Scatter(x = detail_commodity_data['index'], 
                y = detail_commodity_data["Owners' Equivalent Rent QoQ"], 
                name = "Owners' Equivalent Rent",
                line = dict(color = '#FF8911')),
                row = 1,
                col = 3)

    fig.update_layout(template = temp,
                    hovermode = 'closest',
                    margin = dict(l = 20, r = 20, t = 50, b = 50),
                    height = 350, 
                    width = 1200, 
                    showlegend = False,
                    xaxis = dict(tickfont = dict(size = 10)),
                    yaxis = dict(side = "left", tickfont = dict(size=10)),
                    yaxis2 = dict(side = "right", overlaying = "y", tickfont = dict(size=10)))

    return fig 


def plot_cpi_annualized_tend(inflation_data):

    annualized_cpi_data = pd.DataFrame()
    annualized_cpi_data['index'] = inflation_data['index']
    annualized_cpi_data['12M Annualized'] = inflation_data['CPI QoQ'] * 12
    annualized_cpi_data['3M Annualized'] = inflation_data['CPI'].pct_change(3) * 4 * 100
    annualized_cpi_data['6M Annualized'] = inflation_data['CPI'].pct_change(6) * 2 * 100

    annualized_cpi_data['CPI MoM'] = inflation_data['CPI QoQ']
    annualized_cpi_data['Energy CPI MoM'] = inflation_data['Energy CPI QoQ']
    annualized_cpi_data['Food CPI MoM'] = inflation_data['Food CPI QoQ']
    annualized_cpi_data['Electricity CPI MoM'] = inflation_data['Electricity CPI QoQ']
    annualized_cpi_data['Housing CPI MoM'] = inflation_data['Housing CPI QoQ']
    annualized_cpi_data['Oil CPI MoM'] = inflation_data['Oil CPI QoQ']

    fig = make_subplots(rows = 1, cols = 2, subplot_titles = ("Annualized CPI Trend(1M, 3M, 12M)", "Breakdown of CPI MoM"))

    fig.add_trace(
        go.Scatter(x = annualized_cpi_data['index'], 
                y = annualized_cpi_data['12M Annualized'], 
                name = '12 Month Annualized Trend',
                line = dict(color = 'black')),
                row = 1,
                col = 1)
    
    fig.add_trace(
        go.Scatter(x = annualized_cpi_data['index'], 
                y = annualized_cpi_data['3M Annualized'], 
                name = '3 Month Annualized Trend',
                line = dict(color = 'red')),
                row = 1,
                col = 1)
    
    fig.add_trace(
        go.Scatter(x = annualized_cpi_data['index'], 
                y = annualized_cpi_data['6M Annualized'], 
                name = '6 Month Annualized Trend',
                line = dict(color = 'orange')),
                row = 1,
                col = 1)
    
    fig.add_trace(
        go.Scatter(x = annualized_cpi_data['index'], 
                y = annualized_cpi_data['Energy CPI MoM'], 
                name = 'Energy CPI MoM',
                line = dict(color = 'Navy')),
                row = 1,
                col = 2)

    fig.add_trace(
        go.Scatter(x = annualized_cpi_data['index'], 
                y = annualized_cpi_data['Food CPI MoM'], 
                name = 'Food CPI MoM',
                line = dict(color = '#119DFF')),
                row = 1,
                col = 2)
    
    fig.add_trace(
        go.Scatter(x = annualized_cpi_data['index'], 
                y = annualized_cpi_data['Electricity CPI MoM'], 
                name = 'Electricity CPI MoM',
                line = dict(color = '#8c564b')),
                row = 1,
                col = 2)

    fig.add_trace(
        go.Scatter(x = annualized_cpi_data['index'], 
                y = annualized_cpi_data['Oil CPI MoM'], 
                name = 'Oil CPI MoM',
                line = dict(color = '#7f7f7f')),
                row = 1,
                col = 2)


    fig.update_layout(template = temp,
                    hovermode = 'closest',
                    margin = dict(l = 20, r = 20, t = 50, b = 40),
                    height = 350, 
                    width = 1200, 
                    # legend = dict(yanchor = "top",
                    #               orientation = "h",
                    #               y = 0.99,
                    #               xanchor = "left",
                    #               x = 0.01),
                    showlegend = True,
                    xaxis = dict(tickfont = dict(size = 10)),
                    yaxis = dict(side = "left", tickfont = dict(size=10)),
                    yaxis2 = dict(side = "right", overlaying = "y", tickfont = dict(size=10)))

    return fig 


def plot_pce_cpi_indicator_chart(pce_data):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x = pce_data['index'], 
                y = pce_data['PCE MoM'], 
                name = 'PCE MoM',
                line = dict(color = 'red')))

    fig.add_trace(
        go.Scatter(x = pce_data['index'], 
                y = pce_data['CPI QoQ'], 
                name = 'CPI MoM',
                line = dict(color = 'black')))
    
    fig.add_trace(
                    go.Bar(
                        x=pce_data['index'],
                        y=pce_data['CPI MoM - PCE MoM'],
                        name='CPI MoM - PCE MoM',
                        marker=dict(color='navy')  # Set the bar color to 'navy'
                    ))
    

    fig.update_layout(title = "Long Run Difference Between PCE MoM & CPI MoM is approximately equal to 0.25 basis point",
                    title_font = dict(size = 15),
                    width = 1250,
                    height = 500,
                    margin = dict(l = 40, r = 40, t = 40, b = 80),
                    annotations = [dict( text = "Data Source: FRED - Federal Reserve Economic Data",
                                    x = 0,
                                    y = - 0.15,
                                    xref = "paper",
                                    yref = "paper",
                                    showarrow = False)],
                                    
                    yaxis2 = dict(title = "SP500", overlaying = "y", side = "right"),
                    legend = dict(x = 0, y = 1, title = 'Variable'))

    return fig


def plot_inflation_indicator_chart(fred, pce_data):

    ten_year_yield = fred.get_series("DGS10").reset_index(name = '10Y')
    ten_year_yield = ten_year_yield[(ten_year_yield['index'] > pce_data['index'].to_list()[0]) & (ten_year_yield['index'] < pce_data['index'].to_list()[-1])]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x = pce_data['index'], 
                y = pce_data['CPI MoM - PCE MoM Rolling Volatility(12M)'], 
                name = '(CPI MoM - PCE MoM) Rolling Volatility(12M) Indicator',
                line = dict(color = 'black')))

    fig.add_trace(
        go.Scatter(x = ten_year_yield['index'], 
                y = ten_year_yield['10Y'], 
                name = '10Y Yield',
                yaxis = "y2"))

    fig.add_hline(y = pce_data['CPI MoM - PCE MoM Rolling Volatility(12M)'].mean(), 
                  line = dict(dash = 'dash'),
                  name = 'average of indicator')

    fig.update_layout(title = "CPI MoM - PCE MoM Rolling Volatility Indicator v.s. U.S. T-Bill Rate",
                    title_font = dict(size = 15),
                    width = 1300,
                    height = 500,
                    margin = dict(l = 40, r = 40, t = 40, b = 80),
                    annotations = [dict( text = "Data Source: FRED - Federal Reserve Economic Data",
                                    x = 0,
                                    y = - 0.15,
                                    xref = "paper",
                                    yref = "paper",
                                    showarrow = False)],
                                    
                    yaxis2 = dict(title = "U.S. Treasury Yield", overlaying = "y", side = "right"),
                    legend = dict(x = 0, y = 0))

    return fig