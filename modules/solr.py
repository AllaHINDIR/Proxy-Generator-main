import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/core_2')

solr.ping()


solr.add([
    {
        "id": "doc_1",
        "title": "A test document",
    },
    {
        "id": "doc_2",
        "title": "The Banana: Tasty or Dangerous?",
        "_doc": [
            { "id": "child_doc_1", "title": "peel" },
            { "id": "child_doc_2", "title": "seed" },
        ]
    },
])


results = solr.search('doc_1')
print(results.docs)
r = solr.search('*:*')
print(len(r.docs))
solr.delete(q='*:*')
r = solr.search('*:*')
print(len(r.docs))
