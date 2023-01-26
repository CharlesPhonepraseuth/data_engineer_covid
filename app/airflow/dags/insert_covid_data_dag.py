from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

from sqlalchemy import create_engine
import datetime
import os
import pandas as pd


###
### DAG
###

my_dag = DAG(
    dag_id = 'add_new_covid_data_dag',
    tags = ['datascientest', 'covid'],
    schedule_interval = None,
    default_args = {
        'owner': 'airflow',
        'start_date': days_ago(0, minute = 1)
    },
    catchup = False
)

def init():
    postgres_conn = os.environ.get('APP_POSTGRES_CONN')
    conn = create_engine(postgres_conn)

    # get max date from database to allow us
    # to get fresher data from NY Times
    df_covid_date = pd.read_sql('SELECT date FROM covid ORDER BY date DESC LIMIT 1', conn)
    max_covid_date = df_covid_date['date'][0]
    max_covid_date_plus_one = (max_covid_date + datetime.timedelta(days = 1)).strftime('%Y-%m-%d')

    print(max_covid_date)
    print(max_covid_date_plus_one)

    # get current year to automate script
    today = datetime.datetime.now()
    current_year = str(today.year)
    covid_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-" + current_year + ".csv"

    # Int64 allow us to have null value instead of int who raise an error
    dtype_dic = {
        'date': str,
        'county': str,
        'state': str,
        'fips': str,
        'cases': 'Int64',
        'deaths': 'Int64'
    }

    df = pd.read_csv(covid_url, sep = ',', dtype = dtype_dic)

    df_table_counties = pd.read_sql_table('counties', con = conn)
    df_table_states = pd.read_sql_table('states', con = conn)\
                        .rename(columns = {'name': 'state'})

    df_covid = df[['date', 'cases', 'deaths', 'state', 'fips']]

    df_fresh_covid = df_covid[df_covid['date'] == max_covid_date_plus_one]
    print(df_fresh_covid.head())

    # join states and counties table to get state_id and county_id
    df_covid_to_insert = df_fresh_covid.join(df_table_counties.set_index('fips'), on = 'fips', rsuffix = '_county')\
                                       .join(df_table_states.set_index('state'), on = 'state', rsuffix = '_state')\
                                       .drop(columns = ['fips', 'name', 'state_id', 'state'])\
                                       .rename(columns = {'id': 'county_id', 'id_state': 'state_id'})
    # we drop state_id columns from counties table because some county are unknown and have null fips
    # we rename id_state to state_id because we use rsuffix = '_state'

    df_covid_to_insert.to_sql('covid', con = conn, if_exists = 'append', index = False)


init_dag = PythonOperator(
    task_id = 'init_dag',
    python_callable = init,
    dag = my_dag
)
