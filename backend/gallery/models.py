from django.db import models
from django.contrib.auth.models import User  

# Create your models here.


class Pokemon(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    image = models.CharField(max_length=250)


    def __str__(self):
        return self.name
    
class User(models.Model):
    pass

class PokemonData(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)  
    bio = models.CharField(max_length=300)
    ability = models.CharField(max_length=30)
    region = models.CharField(max_length=12)
        
    def __str__(self):
        return self.pokemon
