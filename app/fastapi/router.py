from fastapi import FastAPI

# import controllers
import controllers.covidController as covidController
import controllers.articleController as articleController


app = FastAPI(
    title = 'NY Times project API',
    description = 'API to fetch data',
    version = '1.0.0',
    openapi_tags=[
        {
            'name': 'status',
            'description': 'functions to check if we can connect to the API'
        },
        {
            'name': 'covid',
            'description': 'functions relative to covid'
        },
        {
            'name': 'NYT articles',
            'description': 'functions relative to articles from NYT'
        }
    ]
)


# to check api status
@app.get("/status", tags = ['status'])
def read_status():
    """Check API status
    """
    return {"status": 200}


### covid api route
@app.get("/covid/state/{state:str}", tags = ['covid'])
def read_covid_by_state(state, nb_per_page: int, page_nb: int):
    """Get covid data depends on State 
    """
    covid_data = covidController.get_by_state(state, nb_per_page, page_nb)
    return covid_data


### popular article api route
@app.get("/article/{section:str}", tags = ['NYT articles'])
def read_popular_article(section):
    """Get popular articles 
    """
    articles = articleController.get_popular_article(section)
    return articles
