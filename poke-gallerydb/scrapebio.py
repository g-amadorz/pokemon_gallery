from scrape import getPokemon
import requests
from bs4 import BeautifulSoup as bs
import psycopg2
import threading, time
p = getPokemon()

class PokemonBio:
    def __init__(self, pokemon_id, species, bio, ability, region):
        self.pokemon_id = pokemon_id
        self.species = species
        self.bio = bio
        self.ability = ability
        self.region = region
    
    def toDict(self):
        return {
            'pokemon_id': self.pokemon_id,
            'species': self.species,
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

        
def fetchPokemonBio(pokemon, PokemonBios, lock):
    pokemonName = oddCases(pokemon.get('name'))
    pokemonNum = pokemon.get('num')
    url = f"https://pokemondb.net/pokedex/{pokemonName}"
    response = requests.get(url)
    soup = bs(response.text, 'lxml')

    #Abilities
    ability_cell = soup.find_all('span', class_='text-muted')
    ability = untangle(ability_cell)
    ability_text = onlyOne(ability)

    #Species
    species_cell = soup.find('table', class_='vitals-table',).find_all('td', limit=3)
    species_text = species_cell[2].text

    #Bio
    bio_cell = soup.find('main', id='main').find_all('table', class_='vitals-table', limit=14)[4:14]
    bio_text = filterTags(bio_cell)

    if pokemonName == "Tauros":
        bio_text = "When it targets an enemy, it charges furiously while whipping its body with its long tails"
    

    print(pokemonName)

    #Region
    region = 'Kanto'
    with lock:
        PokemonBios.append(PokemonBio(pokemonNum, species_text, bio_text, ability_text, region).toDict())


def getPokemonBio():
    PokemonBios = []
    lock = threading.Lock()
    threads = []

    for pokemon in p:
        # Create a thread for each Pokémon
        thread = threading.Thread(target=fetchPokemonBio, args=(pokemon, PokemonBios, lock))
        threads.append(thread)  # Add the thread to the list
        thread.start()  # Start the thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join(timeout=10)

    return PokemonBios

# url = f"https://pokemondb.net/pokedex/tauros"
# response = requests.get(url)
# soup = bs(response.text, 'lxml')


# bio_cell = soup.find('main', id='main').find_all('table', class_='vitals-table', limit=14)[4:14]

def filterTags(tags):
    for tag in tags:
        text = tag.find_all('td', class_='cell-med-text')[7:8]
        if text:
            return text[-1].text

bioData = getPokemonBio()

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
    INSERT INTO gallery_pokemondata (pokemon_id, species, bio, ability, region) VALUES (%s, %s, %s, %s, %s)
    '''

    for pokemon in bioData:
        abilities_str = ', '.join(pokemon['ability'])
        cursor.execute(insert_query, (pokemon['pokemon_id'], pokemon['species'], pokemon['bio'], abilities_str, pokemon['region']))
    
    connection.commit()
    print("Data inserted successfully")

except Exception as error:
    print(f"Error: {error}")

finally:
    cursor.close()
    connection.close()








