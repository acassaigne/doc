from pyelasticsearch import ElasticSearch
from es_tools import ES_doc

class Factory(object):

    def __init__(self):
        self.es_connection = None

    def create_es_connection(self):
        if not self.es_connection:
            return ElasticSearch('http://localhost:9200/')
        else:
            return self.es_connection

    def create_es_doc(self):
        return ES_doc(self.create_es_connection())

