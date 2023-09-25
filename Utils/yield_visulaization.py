import numpy as np 
import pandas as pd 
import yfinance as yf

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
temp = dict(layout = go.Layout(font = dict(family="Franklin Gothic", size=12), width = 1500))

def plot_yield_curve(us_treasury_yield_df):

    fig = make_subplots(rows = 1, 
                        cols = 2,
                        subplot_titles = ("10 Year and 3 Month Treasury Yield", "10 Year - 3 Month Yield"))

    fig.add_trace(
        go.Scatter(x = us_treasury_yield_df['index'], 
                y = us_treasury_yield_df['10Y'], 
                name = "10Y Yield",
                line = dict(color = 'black')), row = 1, col = 1)

    fig.add_trace(
        go.Scatter(x = us_treasury_yield_df['index'], 
                y = us_treasury_yield_df['3M'], 
                name = "3M Yield",
                line = dict(color = 'orange')), row = 1, col = 1)

    fig.add_trace(
        go.Scatter(x = us_treasury_yield_df['index'], 
                y = us_treasury_yield_df['10Y'] - us_treasury_yield_df['3M'], 
                name = "10Y minus 3M Yield",
                line = dict(color = 'green')), row = 1, col = 2)

    fig.add_hline(y = 0, row = 1, col = 2, line_dash = "dash", line_color = "red")

    fig.update_layout(template = temp,
                    hovermode = 'closest',
                    margin = dict(l = 20, r = 0, t = 30, b = 20),
                    height = 350, 
                    width = 1200, 
                    showlegend = True,
                    xaxis = dict(tickfont=dict(size=10)),  
                    yaxis = dict(side = "left", tickfont = dict(size=10)),
                    xaxis_showgrid = False)



    return fig 


def plot_3d_yield_curve(us_treasury_yield_df):

    fig = go.Figure(
        data=[go.Surface(x = us_treasury_yield_df.columns, 
                            y = us_treasury_yield_df['index'].values, 
                            z = us_treasury_yield_df.values, 
                            opacity = 0.95,
                            connectgaps = True,
                            colorscale = 'Brwnyl',
                            showscale = True,
                            reversescale = True,)])


    fig.update_layout(title = 'U.S. Treasury Yield Curve Historical Trend', 
                    title_font = dict(size = 15), 
                    hovermode = 'closest',
                    width = 1200,
                    height = 500, 
                    scene = {"aspectratio": {"x": 1, "y": 2.5, "z": 1}, 
                            'camera': {'eye':{'x': 2.5, 'y':0.4, 'z': 1.2}}, 
                            'xaxis_title':'Maturity', 
                            'yaxis_title':'Date', 
                            'zaxis_title':'Yield in %'},
                    margin = dict(l = 10, r = 10, t = 30, b = 50),
                    annotations = [dict(text = "Data Source: FRED - Federal Reserve Economic Data",
                                    x = 0,
                                    y = -0.15,
                                    xref = "paper",
                                    yref = "paper",
                                    showarrow = False)])

    return fig 


def plot_spot_yield_curve(us_treasury_yield_df):

    tabular_df = pd.melt(us_treasury_yield_df.reset_index(drop = True), 
                         id_vars = 'index', 
                         value_vars = us_treasury_yield_df.columns, 
                         var_name = 'Maturity', 
                         value_name = 'Yield')
    
    tabular_df['Date'] = tabular_df['index'].dt.strftime('%Y-%m')

    
    fig = px.line(tabular_df,
                x = 'Maturity',
                y = 'Yield',
                animation_frame = 'Date',
                animation_group = 'Maturity',
                text = tabular_df.Yield)


    fig.update_traces(mode = 'markers+text',
                    textposition = 'top center',
                    textfont = dict(family = 'Arial', size=14),
                    marker = dict(color = 'black'))


    fig.update_layout(title = 'U.S. Treasury Monthly Yield Curve',
                    title_font = dict(size = 15),
                    width = 1200,
                    height = 500,
                    margin = dict(l = 20, r = 0, t = 50, b = 20),
                    annotations = [dict( text = "Data Source: FRED - Federal Reserve Economic Data",
                                        x = 0,
                                        y = - 0.15,
                                        xref = "paper",
                                        yref = "paper",
                                        showarrow = False)])

    fig.update_xaxes(title = None)
    y_min = tabular_df['Yield'].min() * 0
    y_max = tabular_df['Yield'].max() * 1.2 
    fig.update_yaxes(range = [y_min, y_max])

    return fig


def plot_fisher_equation(fred, us_treasury_yield_df):

        ten_year_expected_inflation = fred.get_series('EXPINF10YR').reset_index(name = '10Y expected inflation')
        fed_fund_rate = fred.get_series('DFF').reset_index(name = 'Effective Fed Fund Rate')

        fisher_equation_df = pd.merge(ten_year_expected_inflation, us_treasury_yield_df[['index', '10Y']])
        fisher_equation_df['10Y real rate'] = fisher_equation_df['10Y'] - fisher_equation_df['10Y expected inflation']

        fed_fund_rate = fed_fund_rate[(fed_fund_rate['index'] >= us_treasury_yield_df['index'].to_list()[0]) & (fed_fund_rate['index'] <= us_treasury_yield_df['index'].to_list()[-1])]
        tabular_df = pd.melt(fisher_equation_df, id_vars = 'index', value_vars = fisher_equation_df.columns)
        tabular_df = tabular_df[tabular_df['variable']!='10Y']

        fig = px.bar(tabular_df, 
                x = "index", 
                y = "value", 
                color = "variable",
                color_discrete_sequence = ["#119DFF", "#FF9211"])
        

        fig.add_trace(
                go.Scatter(x = fed_fund_rate['index'], 
                        y = fed_fund_rate['Effective Fed Fund Rate'], 
                        name = "Effective Fed Fund Rate",
                        line = dict(color = 'green')))

        fig.add_trace(
                go.Scatter(x = us_treasury_yield_df['index'], 
                        y = us_treasury_yield_df['10Y'], 
                        name = "10Y",
                        line = dict(color = 'black'),
                        yaxis = 'y2'))
        
        fig.update_layout(title = "Fisher Equation: Nominal Rate = Real Rate + Expected Inflation",
                        title_font = dict(size = 15),
                        width = 1200,
                        height = 500,
                        margin = dict(l = 40, r = 0, t = 40, b = 80),
                        annotations = [dict( text = "Data Source: FRED - Federal Reserve Economic Data",
                                        x = 0,
                                        y = - 0.15,
                                        xref = "paper",
                                        yref = "paper",
                                        showarrow = False)],
                        
                        yaxis = dict(title = "Yield (%)"),
                        yaxis2 = dict(title = "Yield (%)", overlaying = "y", side = "right"),
                        legend = dict(x = 0, y = 1))
        
        fig.update_xaxes(title = 'Datetime')
        fig.update_yaxes(title = "U.S. T-Bill Rate",  secondary_y = True)

        return fig


def plot_move_index(us_treasury_yield_df):

    move_index = yf.download("^MOVE")
    us_treasury_yield_df = us_treasury_yield_df[(us_treasury_yield_df['index'] > move_index.index.to_list()[0])]

    fig = go.Figure()

    fig.add_trace(
    go.Scatter(x = us_treasury_yield_df['index'], 
            y = us_treasury_yield_df['10Y'], 
            line = dict(color = 'black'),
            name = '10Y Yield'))

    fig.add_trace(
        go.Scatter(x = move_index.index,
                y = move_index['Close'],
                name = 'ICE BofAML MOVE Index',
                yaxis = 'y2')
    )

    fig.update_layout(title = "MOVE Index & U.S. T-Bill Rate",
                title_font = dict(size = 15),
                width = 1300,
                height = 500,
                margin = dict(l = 40, r = 40, t = 40, b = 80),
                annotations = [dict( text = "Data Source: FRED - Federal Reserve Economic Data & Yahoo Finance",
                                x = 0,
                                y = - 0.15,
                                xref = "paper",
                                yref = "paper",
                                showarrow = False)],
                                
                yaxis2 = dict(title = "Move Index", overlaying = "y", side = "right"),
                legend = dict(x = 0, y = 0))


    return fig