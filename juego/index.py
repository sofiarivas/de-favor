from django.contrib.algoliasearch import AlgoliaIndex

class JuegoIndex(AlgoliaIndex):
    fields = ('titulo',)
    settings = {'attributesToIndex': ['titulo', ]
    }
