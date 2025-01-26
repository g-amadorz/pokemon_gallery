from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Pokemon, User
from .serializers import PokemonSerializer, UserSerializer
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

@api_view(["GET"])
def getRandomPokemon(request):
    count = int(request.GET.get('count', 5))
    queryset = Pokemon.objects.all()
    randomPokemon = random.sample(list(queryset), count)

    serializer = PokemonSerializer(randomPokemon, many=True)

    return Response(serializer.data)




# @api_view(["POST"])
# def createUser(request):
#     queryset = User.objects.all
#     serializer_class = UserSerializer()
