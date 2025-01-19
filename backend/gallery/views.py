from django.shortcuts import render
from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random


class PokemonListCreate(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    lookup_field = 'pk'

class PokemonListView(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


@api_view(["GET"])
def getRandomPokemon(request):
    queryset = Pokemon.objects.all()
    randomPokemon = random.sample(list(queryset), k=random.randint(5, 8))

    serializer = PokemonSerializer(randomPokemon, many=True)

    return Response(serializer.data)