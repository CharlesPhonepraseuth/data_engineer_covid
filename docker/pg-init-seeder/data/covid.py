import pandas as pd
import time


def init_covid_data(conn):
    """ Get covid data from ny times github, and then insert it into postgres """

    years = ['2020', '2021', '2022'] 

    for index, year in enumerate(years):
        url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-" + year + ".csv"
        print('===== url :' + url + ' =====')

        # Int64 allow us to have null value instead of int who raise an error
        dtype_dic = {
            'date': str,
            'county': str,
            'state': str,
            'fips': str,
            'cases': 'Int64',
            'deaths': 'Int64'
        }

        df = pd.read_csv(url, sep = ',', dtype = dtype_dic)
        print(df.head())

        # to avoid useless process, we only once insert into states and counties table
        if index == 0:
            ###
            ### insert into states table
            ###
            df_states = df['state'].rename('name')\
                                   .drop_duplicates(keep = 'first')

            start_time = time.time()
            df_states.to_sql('states', con = conn, if_exists = 'append', index = False)
            print("STATES to_sql duration: {} seconds".format(time.time() - start_time))

            df_table_states = pd.read_sql_table('states', con = conn)
            print(df_table_states.head())


            ###
            ### insert into counties table
            ###
            df_counties = df[['county', 'fips', 'state']].rename(columns = {'state': 'name'})\
                                                         .drop_duplicates(subset = 'fips', keep = 'first')

            # join states table to get state_id
            df_counties_to_insert = df_counties.join(df_table_states.set_index('name'), on = 'name')\
                                               .drop(columns = 'name')\
                                               .rename(columns = {'county': 'name', 'id': 'state_id'})

            start_time = time.time()
            df_counties_to_insert.to_sql('counties', con = conn, if_exists = 'append', index = False)
            print("COUNTIES to_sql duration: {} seconds".format(time.time() - start_time))

            df_table_counties = pd.read_sql_table('counties', con = conn)
            print(df_table_counties.head())


        ###
        ### insert into covid table
        ###
        df_table_counties = pd.read_sql_table('counties', con = conn)
        df_table_states = pd.read_sql_table('states', con = conn)\
                            .rename(columns = {'name': 'state'})

        df_covid = df[['date', 'cases', 'deaths', 'state', 'fips']]

        # join states and counties table to get state_id and county_id
        df_covid_to_insert = df_covid.join(df_table_counties.set_index('fips'), on = 'fips', rsuffix = '_county')\
                                     .join(df_table_states.set_index('state'), on = 'state', rsuffix = '_state')\
                                     .drop(columns = ['fips', 'name', 'state_id', 'state'])\
                                     .rename(columns = {'id': 'county_id', 'id_state': 'state_id'})
        # we drop state_id columns from counties table because some county are unknown and have null fips
        # we rename id_state to state_id because we use rsuffix = '_state'

        start_time = time.time()
        df_covid_to_insert.to_sql('covid', con = conn, if_exists = 'append', index = False)
        print("COVID to_sql duration: {} seconds".format(time.time() - start_time))

        df_table_covid = pd.read_sql_table('covid', con = conn)
        print(df_table_covid.sort_values(by = 'date', ascending = False).head())
