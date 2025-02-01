from rest_framework import serializers
from .models import Pokemon, PokemonData, User


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['num', 'name', 'type', 'image']

class PokemonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonData
        fields = ['pokemon', 'region', 'ability', 'bio']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'liked_pokemon']


