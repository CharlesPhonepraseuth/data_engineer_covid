from common.utils.elasticsearch import get_es_client
from mappings import news_mapping, articles_mapping, popular_mapping


es = get_es_client()

# create news index
print("Indexing and mapping news index... (please hold on)")
es.indices.create(index = 'news', mappings = news_mapping)
print("...done indexing")

# create articles index
print("Indexing and mapping articles index... (please hold on)")
es.indices.create(index = 'articles', mappings = articles_mapping)
print("...done indexing")

# create popular index
print("Indexing and mapping popular index... (please hold on)")
es.indices.create(index = 'popular', mappings = popular_mapping)
print("...done indexing")
