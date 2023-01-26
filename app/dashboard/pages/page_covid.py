### Import Packages ###
import dash 
from dash import dcc, html

### Import Dash Instance and Custom Functions ###
from app import app
from pages.partials import navbar
from controllers import covid_ct
from callbacks import covid_cb


### Get Data ###
covid_data = covid_ct.get_data()

newest_date_str = covid_data['newest_date_str']
global_cases_clean = covid_data['global_cases_clean']
global_deaths_clean = covid_data['global_deaths_clean']
latest_day_cases_clean = covid_data['latest_day_cases_clean']
latest_day_deaths_clean = covid_data['latest_day_deaths_clean']
fig_cases_30d = covid_data['fig_cases_30d']
fig_deaths_30d = covid_data['fig_deaths_30d']
states_dropdown_options = covid_data['states_dropdown_options']
counties_dropdown_options = covid_data['counties_dropdown_options']


### Create Layout ###
layout = html.Div([
    navbar.create_navbar(),

    html.Br(),

    html.H1("Dashboard covid", style = {'textAlign': 'center', 'color': '#343A40'}),

    html.Br(),

    html.Div([
        html.Div([
            html.H6('Cas cumulés',
                    style = {'textAlign': 'center', 'color': 'orange'}
            ),
            html.P(global_cases_clean,
                    style = {'textAlign': 'center', 'color': 'orange', 'fontSize': 40}
            ),
            html.P(newest_date_str + ' : +' + latest_day_cases_clean, style = {'textAlign': 'center', 'color': 'orange', 'fontSize': 15, 'margin-top': '-18px'}
            )
        ]),
        html.Div([
            html.H6('Morts cumulés',
                    style = {'textAlign': 'center', 'color': '#dd1e35'}
            ),
            html.P(global_deaths_clean,
                    style = {'textAlign': 'center', 'color': '#dd1e35', 'fontSize': 40}
            ),
            html.P(newest_date_str + ' : +' + latest_day_deaths_clean, style = {'textAlign': 'center', 'color': '#dd1e35', 'fontSize': 15, 'margin-top': '-18px'}
            )
        ]),
    ], style = {'display': 'flex', 'justify-content': 'space-evenly'}),

    html.Br(),

    html.Div([
        html.Div(dcc.Graph(figure = fig_cases_30d), style = {'flex': 1}),
        html.Div(dcc.Graph(figure = fig_deaths_30d), style = {'flex': 1}),
    ], style = {'display': 'flex'}),

    html.Br(),

    html.Div([
        html.Div([
            html.P('États :', style = {'font-weight': 'bold'}),
            html.Div(dcc.Dropdown(id = 'page-covid-states-dropdown',
                                  options = states_dropdown_options,
                                  value = states_dropdown_options[0]['value']
            )),
        ], style = {'width': '30vw'}),
        html.Div([
            html.P('Comtés :', style = {'font-weight': 'bold'}),
            html.Div(dcc.Dropdown(id = 'page-covid-counties-dropdown',
                                  options = counties_dropdown_options,
                                  value = counties_dropdown_options[0]['value']
            )),
        ], style = {'width': '30vw'}),
    ], style = {'display': 'flex', 'justify-content': 'space-evenly'}),
    html.Div([
        html.Div(dcc.Graph(id = 'page-covid-graph-cases'), style = {'flex': 1}),
        html.Div(dcc.Graph(id = 'page-covid-graph-deaths'), style = {'flex': 1})
    ], style = {'display': 'flex'})
])


### Register Callbacks ###
covid_cb.register_callbacks(app, covid_data['df_covid'])
