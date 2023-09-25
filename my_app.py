import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, use_pages = True)

app.layout = html.Div([
        # main app framework
        html.Div([
            
        html.Div(children = ["U.S. Treasury Bill Market Analysis - By Ken Chiang"], 
                 style = {'fontSize':40, 
                        'textAlign':'center',
                        'margin-top' : '10px',
                        'margin-bottom': '20px'}),

        html.A(id = 'gh-link', 
               children = ['View on GitHub'], 
               href = "https://github.com/KenChiang1997/Real-Time-Paper-Trading-Bot", 
               style = {'color': 'white', 
                        'font-size': '15px', 
                        'color': '#fff', 
                        'border': 'solid 1px #fff',
                        'border-radius': '2px', 
                        'padding': '0px', 
                        'padding-top': '-30px', 
                        'padding-right': '15px', 
                        'font-weight': '200', 
                        'position': 'relative', 
                        'top': '0px', 
                        'float': 'right', 
                        'margin-top': '20px',
                        'margin-right': '40px', 
                        'margin-left': '2px', 
                        'transition-duration': '400ms',}), 

        html.Div(className = "div-logo",
                children = html.Img(className="logo", src=("https://opendatabim.io/wp-content/uploads/2021/12/GitHub-Mark-Light-64px-1.png"), 
                style = {'height': '60px','padding': '30px', 'margin-top': '-30px'}), 
                style={'display': 'inline-block', 'float': 'right'}),

        html.Div([dcc.Link(page['name'], 
                           href = page['path'],
                           style={'fontSize': 15,
                                   'padding': '10px',
                                   'color': '#fff', 
                                   'border': 'solid 1px #fff',
                                   'margin-top': '-30px',
                                   'margin': '10px'})
                            for page in dash.page_registry.values()], style={'textAlign': 'center',
                                                                             'margin-left': '260px'}),

                    ],style = {"background": "#2c5c97", 
                            "color": "white", 
                            "padding-top": "30px", 
                            "padding-left": "48px",
                            "padding-bottom": "50px", 
                            "padding-left": "24px"}),


        html.Hr(),
        # content of each page
        dash.page_container
    ]
)


if __name__ == "__main__":
    app.run(debug=True)