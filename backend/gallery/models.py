from django.db import models  

# Create your models here.


class Pokemon(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    image = models.CharField(max_length=250)


    def __str__(self):
        return self.name
    
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    favourites = models.ManyToManyField(Pokemon, related_name="favourite")


class PokemonData(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)
    ability = models.CharField(max_length=30)
    region = models.CharField(max_length=12)
