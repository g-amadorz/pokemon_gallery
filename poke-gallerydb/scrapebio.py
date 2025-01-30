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
            'bio': self.bio,
            'ability': self.ability,
            'region': self.region
        }

def untangle(cell):
    if len(cell) == 1:
        cell = [cell[0].text]
    else:
        cell = [makeNice(cell[0].text), makeNice(onlyOne(cell[1].text))]
        if cell[1] == None:
            cell = [cell[0]]
    return cell

def oddCases(pokemonName):
    if ("Nidoran♀" == pokemonName):
        pokemonName = 'Nidoran-f'
    elif ('Nidoran♂' == pokemonName):
        pokemonName = 'Nidoran-m'
    elif ("Farfetch'd" == pokemonName):
        pokemonName = 'Farfetchd'
    elif('Mr. Mime' == pokemonName):
        pokemonName = 'mr-mime'
    return pokemonName

def onlyOne(ability):
    if ('#' in ability):
        ability = None
    return ability

def makeNice(ability):
    if ability == None:
        return
    ability = ability.replace("1.", "").replace("2.","").strip()
    return ability

        
def getPokemonBio():
    PokemonBios = []
    for pokemon in p:
        pokemonName = oddCases(pokemon.get('name'))
        url = f"https://pokemondb.net/pokedex/{pokemonName}"
        response = requests.get(url)
        soup = bs(response.text, 'lxml')

        #Abilities
        ability_cell = soup.find_all('span', class_='text-muted')
        ability = untangle(ability_cell)
        ability_text = onlyOne(ability)

        #Bio
        species_cell = soup.find('table', class_='vitals-table',).find_all('td', limit=3)
        species_text = species_cell[2].text


        #Region
        region = 'Kanto'

        PokemonBios.append(PokemonBio(pokemonName, species_text, ability_text, region).toDict())


    return PokemonBios

PokemonsData = getPokemonBio()

try:
    connection = psycopg2.connect(
        dbname="pokedb",
        user="postgres",
        password="docker",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()

    # Insert data into table
    insert_query = ''' 
    INSERT INTO gallery_pokemon (num, name, type, image) VALUES (%s, %s, %s, %s)
    '''

    for pokemon in PokemonsData:
        types_str = ', '.join(pokemon['ability'])
        cursor.execute(insert_query, (pokemon['num'], pokemon['name'], types_str, pokemon['sprite']))
    
    connection.commit()
    print("Data inserted successfully!")

except Exception as error:
    print(f"Error: {error}")

finally:
    cursor.close()
    connection.close()


