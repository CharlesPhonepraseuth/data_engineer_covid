from common.utils.postgres import get_pg_client
from data.covid import init_covid_data
import pandas as pd


db = get_pg_client()
conn = db.connect()

df_table_covid = pd.read_sql_table('covid', con = conn)

# we only insert if the table is empty
if df_table_covid.empty:
    # start insert data
    init_covid_data(conn)

# close connection
conn.close()
