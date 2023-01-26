from elasticsearch import helpers
from pprintpp import pprint
import requests
import time
import os

from common.utils.elasticsearch import get_es_client


es = get_es_client()

NY_TIMES_API_KEY = os.environ.get('NY_TIMES_API_KEY')

###
### NEWSWIRE API
###

news_endpoint = "https://api.nytimes.com/svc/news/v3/content/all/all.json"

news_params = {
    "api-key": NY_TIMES_API_KEY
}

news_response = requests.get(news_endpoint, params = news_params)
news = news_response.json()

news_rows = []

for row in news["results"]:
    data_formated = {
        'slug_name':            row['slug_name'],
        'section':              row['section'],
        'subsection':           row['subsection'],
        'title':                row['title'],
        'abstract':             row['abstract'],
        'url':                  row['url'],
        'byline':               row['byline'],
        'source':               row['source'],
        'updated_date':         row['updated_date'],
        'created_date':         row['created_date'],
        'published_date':       row['published_date'],
        'first_published_date': row['first_published_date'],
        'material_type_facet':  row['material_type_facet'],
        'des_facet':            row['des_facet'],
        'org_facet':            row['org_facet'],
        'per_facet':            row['per_facet'],
        'geo_facet':            row['geo_facet']
    }

    news_rows.append(data_formated)

# insert into news index
print("Insert into news index... (please hold on)")
helpers.bulk(es, news_rows, index = 'news')
print("...done inserting")


###
### ARTICLES API
###

articles_endpoint = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

articles_params = {
    "api-key": NY_TIMES_API_KEY
}

articles_response = requests.get(articles_endpoint, params = articles_params)
articles = articles_response.json()

articles_rows = []

for row in articles["response"]["docs"]:
    data_formated = {
        'article_id':       row['_id'],
        'web_url':          row['web_url'],
        'abstract':         row['abstract'],
        'snippet':          row['snippet'],
        'lead_paragraph':   row['lead_paragraph'],
        'source':           row['source'] if 'source' in row else None,
        'headline':         row['headline']['main'],
        'keywords':         row['keywords'],
        'pub_date':         row['pub_date'],
        'document_type':    row['document_type'],
        'news_desk':        row['news_desk'],
        'section_name':     row['section_name'],
        # some rows haven't subsection_name
        'subsection_name':  row['subsection_name'] if 'subsection_name' in row else None,
        'byline':           row['byline'],
        'word_count':       row['word_count']
    }

    articles_rows.append(data_formated)

# insert into articles index
print("Insert into articles index... (please hold on)")
helpers.bulk(es, articles_rows, index = 'articles')
print("...done inserting")


###
### POPULAR API
###

time.sleep(45)

cat=["emailed","viewed"]
popular_rows = []
for pop_type in cat:
    print(pop_type)
    popular_endpoint = "https://api.nytimes.com/svc/mostpopular/v2/{}/1.json".format(pop_type)
    news_params = {
        "api-key": NY_TIMES_API_KEY

    }

    popular_response = requests.get(popular_endpoint, params = news_params)
    popular = popular_response.json()

    for row in popular["results"]:

        data_formated = {
            'popular_type':         pop_type,
            "days":                 1,
            'article_uri':          row.get('uri'),
            'article_url':          row.get('url'),
            'id':                   row.get('id'),
            'source':               row.get('source'),
            'pub_date':             row.get('published_date'),
            'article_section':      row.get('section'),
            'article_subsection':   row.get('subsection'),
            'article_nytdsection':  row.get('nytdsection'),
            'article_adx_keywords': row.get('adx_keywords'),
            'byline':               row.get('byline'),
            'article_type':         row.get('type'),
            'article_title':        row.get('title'),            
            'article_abstract':     row.get('abstract'),
        }

        popular_rows.append(data_formated)


# insert into articles index
print("Insert into articles index... (please hold on)")
helpers.bulk(es, popular_rows, index = 'popular')
print("...done inserting")
