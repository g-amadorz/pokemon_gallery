from rest_framework import serializers
from .models import Pokemon, PokemonData

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['num', 'name', 'type', 'image']

class PokemonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonData
        fields = ['pokemon', 'region', ]


