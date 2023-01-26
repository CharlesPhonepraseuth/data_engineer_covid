### Import Packages ###
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import os

### Import Dash Instance and Pages ###
from app import app
from pages.partials import navbar
from pages import page_covid


### Set app layout ###
app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

### Index Page Layout ###
index_page = html.Div([
    navbar.create_navbar(),
    html.Br(),
    html.H1('Application de visualisation', style = {'color' : '#343A40', 'textAlign': 'center'})
], style = {'alignItems': 'center', 'min-height': '101vh'})

### Update Page Container ###
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/covid':
        return page_covid.layout
    else:
        return index_page


if __name__ == '__main__':
    port = os.environ.get('DASH_HTTP_PORT')

    app.run_server(debug = True, host = '0.0.0.0', port = port)
