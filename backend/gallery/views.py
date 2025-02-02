from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from .models import Pokemon, User, PokemonData
from .serializers import PokemonSerializer, UserSerializer, PokemonDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from django.http import HttpResponse

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

class RandomPokemon(APIView):
    def get(self, request, *args, **kwargs):
        count = int(request.GET.get('count', 5))

        all_pks = Pokemon.objects.values_list('pk', flat=True)

        random_pks = random.sample(list(all_pks), count)

        randomPokemon = Pokemon.objects.filter(pk__in=random_pks)

        classSerializer = PokemonSerializer(randomPokemon, many=True)

        return Response(classSerializer.data)
    
class SortByPokemonType(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        try:
            type = str(request.GET.get('type', 'Psychic'))
            
            queryset = Pokemon.objects.filter(type__icontains=type)

            classSerializer = PokemonSerializer(queryset, many=True)

            return Response(classSerializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


class PickPokemon(viewsets.ViewSet):
    def show(self, request, *args, **kwargs):
        try:
            pokemonQuery = str(request.GET.get('pokemon', 'Mew'))

            pokemonKey = Pokemon.objects.get(name=pokemonQuery).id

            pokemonInfo = PokemonData.objects.get(pokemon_id=pokemonKey)

            classSerializer = PokemonDataSerializer(pokemonInfo)

            return Response(classSerializer.data)

        except Exception as e:
            return Response(f'Error {e}')


# @api_view(["POST"])
# def createUser(request):
#     queryset = User.objects.all
#     serializer_class = UserSerializer()
