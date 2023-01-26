from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError
import os
import time


def get_es_client():

    ELASTICSEARCH_HTTP_PORT = int(os.environ.get('ELASTICSEARCH_HTTP_PORT'))

    es = Elasticsearch(hosts = [{"host": "elasticsearch", "port": ELASTICSEARCH_HTTP_PORT, "scheme": "http"}], retry_on_timeout = True)
    es.options(ignore_status = 400)

    for _ in range(100):
        try:
            # make sure the cluster is available
            es.cluster.health(wait_for_status = "yellow")
        except ConnectionError:
            time.sleep(2)

    return es
