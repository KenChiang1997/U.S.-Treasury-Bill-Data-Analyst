import dash
from dash import html, dcc,  dash_table

from fredapi import Fred 
from Utils.yield_module import get_treasury_data, get_yield_change_df
from Utils.yield_visulaization import plot_3d_yield_curve, plot_spot_yield_curve, plot_fisher_equation, plot_yield_curve, plot_move_index

dash.register_page(__name__) 

api_key = 'a0aee094a9b908bd7c16baece8df8419'
fred = Fred(api_key = 'a0aee094a9b908bd7c16baece8df8419')


us_treasury_yield_df = get_treasury_data(fred)
yield_change_df = get_yield_change_df(us_treasury_yield_df)

simple_yield_curve_chart = plot_yield_curve(us_treasury_yield_df.tail(720))
three_d_yield_curve_chart = plot_3d_yield_curve(us_treasury_yield_df.tail(720))
spot_curve_chart = plot_spot_yield_curve(us_treasury_yield_df.tail(720))
fisher_equation_chart = plot_fisher_equation(fred, us_treasury_yield_df)
move_index_chart = plot_move_index(us_treasury_yield_df)


layout = html.Div(
    [
        # Heder Setting
        html.Div([html.H1(children = "Treasury Yield Trend, Data Source: FRED - Federal Reserve Economic Data", 
                          style = {'textAlign': 'center', 'font-size': '25px', 'text-align': 'left'})]),

        html.P(children = "1.1) Yield Movement & Yield Spread",
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
                                  
        dcc.Graph(id = "Yield_Spread_Chart", figure = simple_yield_curve_chart, style = {'margin-left' : '10px' }),

        dash_table.DataTable(data = yield_change_df.reset_index().to_dict('records'), 
                            style_cell = {'textAlign': 'right'},
                            style_cell_conditional = [{'if': {'column_id': 'open_time'},'textAlign': 'left'}],
                            style_header = {'backgroundColor': '#2c5c97', 'fontWeight': 'bold', 'color':'#D1D9DB', 'font-size': '18px', 'textAlign': 'center'},
                            style_data = {'backgroundColor': 'White', "whiteSpace": 'auto', "height":"auto", 'textAlign': 'center', 'font-size': '15px'},
                            style_table = {'width': '1250px', 'overflowY': 'auto', 'margin-top': '10px', 'margin-left' : '20px'}),

        html.P(children = "1.2) Yield Curve",
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
                                  
        dcc.Graph(id = "Yield_Curve_Chart", figure = spot_curve_chart, style = {'margin-left' : '10px' }),

        html.P(children = "1.3) 3D Yield Curve Trend",
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
                                  
        dcc.Graph(id = "3D_Yield_Curve_Chart", figure = three_d_yield_curve_chart, style = {'margin-left' : '10px' }),

        html.P(children = "1.4) Fisher Equation Chart",
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
                                  
        dcc.Graph(id = "Fisher_Equation_Chart", figure = fisher_equation_chart, style = {'margin-left' : '10px' }),

        html.P(children = "1.5) ICE BofAML MOVE Index",
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
                                  
        dcc.Graph(id = "Move_Index_Chart", figure = move_index_chart, style = {'margin-left' : '10px' }),
    ]
)