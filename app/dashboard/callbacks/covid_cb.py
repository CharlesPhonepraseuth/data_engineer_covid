from dash.dependencies import Output, Input
import plotly.express as px


def register_callbacks(app, df_covid):

    @app.callback(Output(component_id = 'page-covid-counties-dropdown', component_property = 'options'),
                  [Input(component_id = 'page-covid-states-dropdown', component_property = 'value')])
    def update_counties_dropdown(state):

        if state == 'all':
            return [{'label': 'Tous...', 'value': 'all'}]
        else:
            df_counties = df_covid[df_covid['state'] == state]['county'].dropna().sort_values().unique().tolist()

            counties_dropdown_options = [{'label': state, 'value': state} for state in df_counties]
            counties_dropdown_options[0] = {'label': 'Tous...', 'value': 'all'}

            return counties_dropdown_options


    @app.callback(Output(component_id = 'page-covid-graph-cases', component_property = 'figure'),
                  [Input(component_id = 'page-covid-states-dropdown', component_property = 'value'),
                   Input(component_id = 'page-covid-counties-dropdown', component_property = 'value')])
    def update_graph_cases(state, county):

        if state == 'all':
            df_filtered = df_covid
        else:
            if county == 'all':
                df_filtered = df_covid[df_covid['state'] == state]
            else:
                df_filtered = df_covid[(df_covid['state'] == state) & (df_covid['county'] == county)]
        
        df_to_render = df_filtered.groupby(['date']).agg({'cases': sum}).reset_index()

        fig_cases = px.line(df_to_render, x = "date", y = "cases")
        fig_cases.update_layout(yaxis_title = 'cas')

        return fig_cases


    @app.callback(Output(component_id = 'page-covid-graph-deaths', component_property = 'figure'),
                  [Input(component_id = 'page-covid-states-dropdown', component_property = 'value'),
                   Input(component_id = 'page-covid-counties-dropdown', component_property = 'value')])
    def update_graph_deaths(state, county):

        if state == 'all':
            df_filtered = df_covid
        else:
            if county == 'all':
                df_filtered = df_covid[df_covid['state'] == state]
            else:
                df_filtered = df_covid[(df_covid['state'] == state) & (df_covid['county'] == county)]
        
        df_to_render = df_filtered.groupby(['date']).agg({'deaths': sum}).reset_index()

        fig_deaths = px.line(df_to_render, x = "date", y = "deaths")
        fig_deaths.update_layout(yaxis_title = 'morts')

        return fig_deaths
