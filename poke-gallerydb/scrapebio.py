from scrape import getPokemon
import requests
from bs4 import BeautifulSoup as bs
import psycopg2

p = getPokemon()

class PokemonBio:
    def __init__(self, pokemon, bio, ability, region):
        self.pokemon = pokemon
        self.bio = bio
        self.ability = ability
        self.region = region
    
    def toDict(self):
        return {
            'pokemon': self.pokemon,
            'name': self.bio,
            'ability': self.ability,
            'region': self.region
        }

def getPokemonBio():
    PokemonBios = []
    for pokemon in p:
        url = f"https://pokemondb.net/pokedex/{pokemon.name}"
        response = requests.get(url)
        soup = bs(response.text, 'lxml')
        rows = soup.find_all('div', class_='grid-col span-md-6 span-lg-4 text-center')

        print(rows)

        #PokemonBios.append(PokemonBio().toDict())


    #return PokemonBios








