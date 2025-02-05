from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pokemons', views.PokemonListCreate)

urlpatterns = [
    path('create/', views.PokemonListCreate.as_view(), name='create'),
    path('pokemons/<int:pk>/', views.PokemonListRetrieveUpdateDestroy.as_view(), name='pokemon'),
    path('pokemons/all/', views.PokemonListView.as_view(), name='pp'),
    path('pokemons/all/random/', views.RandomPokemon.as_view(), name="random"),
    path('pokemons/types/', views.SortByPokemonType.as_view({'get': 'list'}), name="find types"),
    path('pokemons/get/', views.getPokemonInfo.as_view({'get': 'list'}), name='get')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)