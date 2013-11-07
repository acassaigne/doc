from pyelasticsearch import ElasticSearch

es = ElasticSearch('http://localhost:9200/')

query = {
   "query" : {
      "text" : {
         "my_attachment" : "imprimante"
      }
   }
}

result = es.search(query, index='attach77')

print result
