def get_data():
    ### Import Packages ###
    import plotly.express as px
    import pandas as pd
    from datetime import datetime, date, timedelta

    ### Import custom function ###
    from common.utils import postgres


    # manipulate data to render into layout
    conn = postgres.get_pg_client()

    df_table_covid = pd.read_sql_table('covid', con = conn)
    df_table_states = pd.read_sql_table('states', con = conn)
    df_table_counties = pd.read_sql_table('counties', con = conn)

    # join tables to get full dataframe
    df_covid = df_table_covid.join(df_table_states.set_index('id'), on = 'state_id', rsuffix = '_state')\
                             .join(df_table_counties.set_index('id'), on = 'county_id', rsuffix = '_county')\
                             .drop(columns = ['id', 'fips', 'state_id_county', 'state_id', 'county_id'])\
                             .rename(columns = {'name': 'state', 'name_county': 'county'})

    if df_covid.empty:

        global_cases_clean = 'x'
        global_deaths_clean = 'x'
        newest_date_str = 'xx/xx/xx'
        latest_day_cases_clean = 'x'
        latest_day_deaths_clean = 'x'
        states_dropdown_options = [{'label': 'Tous...', 'value': 'all'}]
        counties_dropdown_options = [{'label': 'Tous...', 'value': 'all'}]

        data = {'value1': [0, 1, 2], 'value2': [0, 1, 2]}
        df = pd.DataFrame(data)

        fig_cases_30d = px.line(df, x = "value1", y = "value2")
        fig_deaths_30d = px.line(df, x = "value1", y = "value2")

    else:

        # str format is yyyy-mm-dd hh:MM:ss so we split it to only get date
        newest_date_from_df_str = str(df_covid['date'].max()).split(' ')[0]
        # we transform to date object to allow us to get last 30 days date
        newest_date = datetime.strptime(newest_date_from_df_str, '%Y-%m-%d').date()
        # we transform date object to str with fr format
        newest_date_str = newest_date.strftime("%d/%m/%Y")


        # get latests data
        df_covid_latest_day = df_covid[df_covid['date'] == str(newest_date)]

        global_cases = int(df_covid_latest_day['cases'].sum())
        global_cases_clean = format(global_cases, ',d')

        global_deaths = int(df_covid_latest_day['deaths'].sum()) 
        global_deaths_clean = format(global_deaths, ',d')

        
        # we get yesterday to compare from current day
        date_yesterday = str(newest_date - timedelta(days = 1))
        df_covid_yesterday = df_covid[df_covid['date'] == date_yesterday]
  
        # format for UX (ex : 270,400,821)
        latest_day_cases = int(df_covid_yesterday['cases'].sum())
        latest_day_cases_clean = format(global_cases - latest_day_cases, ',d')

        latest_day_deaths = int(df_covid_yesterday['deaths'].sum())
        latest_day_deaths_clean = format(global_deaths - latest_day_deaths, ',d')

        # get last 30 days from latest date
        date_30d_before = str(newest_date - timedelta(days = 30))
        df_covid_30d = df_covid[df_covid['date'] >= date_30d_before]

        df_covid_by_date_30d = df_covid_30d[['date', 'cases', 'deaths']].groupby('date').sum(numeric_only = True).reset_index()

        # create cases figure
        fig_cases_30d = px.line(df_covid_by_date_30d, x = "date", y = "cases")
        fig_cases_30d.update_layout(title_text = 'Cas confirmés - 30 derniers jours', title_x = 0.5, yaxis_title = 'cas')
        # create deaths figure
        fig_deaths_30d = px.line(df_covid_by_date_30d, x = "date", y = "deaths")
        fig_deaths_30d.update_layout(title_text = 'Morts confirmés - 30 derniers jours', title_x = 0.5, yaxis_title = 'morts')

        # get unique states for dropdown
        df_states = df_covid['state'].dropna().sort_values().unique().tolist()
        states_dropdown_options = [{'label': state, 'value': state} for state in df_states]
        states_dropdown_options[0] = {'label': 'Tous...', 'value': 'all'}
        # get default counties dropdown
        counties_dropdown_options = [{'label': 'Tous...', 'value': 'all'}]

    data = {
        'global_cases_clean': global_cases_clean,
        'global_deaths_clean': global_deaths_clean,
        'newest_date_str': newest_date_str,
        'latest_day_cases_clean': latest_day_cases_clean,
        'latest_day_deaths_clean': latest_day_deaths_clean,
        'states_dropdown_options': states_dropdown_options,
        'counties_dropdown_options': counties_dropdown_options,
        'fig_cases_30d': fig_cases_30d,
        'fig_deaths_30d': fig_deaths_30d,
        'df_covid': df_covid
    }

    return data
