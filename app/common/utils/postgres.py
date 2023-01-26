from sqlalchemy import create_engine
import os


def get_pg_client():

    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')
    host = os.environ.get('POSTGRES_HOST')
    port = os.environ.get('POSTGRES_HTTP_PORT')
    database = os.environ.get('POSTGRES_DB')

    db_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(user, password, host, port, database)
    db = create_engine(db_string)

    return db
