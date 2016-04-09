from django.apps import AppConfig
from django.contrib import algoliasearch
from .index import JuegoIndex

class JuegoConfig(AppConfig):
    name = 'juego'

    def ready(self):
	    Juego = self.get_model('juego')
	    algoliasearch.register(Juego, JuegoIndex)

