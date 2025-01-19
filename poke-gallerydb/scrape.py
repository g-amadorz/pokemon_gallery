import requests
from bs4 import BeautifulSoup as bs
import psycopg2


class Pokemon:
    def __init__(self, num, name, types, sprite):
        self.num = num
        self.name = name
        self.types = types
        self.sprite = sprite

    def toDict(self):
        return {
            'num': self.num,
            'name': self.name,
            'types': self.types,
            'sprite': self.sprite
            }

PokemonsData = []

#URL to scrape: BeautifulSoup setup
url = 'https://pokemondb.net/pokedex/game/firered-leafgreen'
response = requests.get(url)
soup = bs(response.text, 'lxml')
rows = soup.find_all('div', class_='infocard')

num = 1

#Loops over each row in the table
for row in rows:

    pokemon_data_cell = row.find('span', class_='infocard-lg-data text-muted')

    pokemon_image_cell = row.find('span', class_='infocard-lg-img')

    name = pokemon_data_cell.find('a', class_='ent-name').text

    #num = pokemon_data_cell.find('small').text.replace('#', '') #Removes the # from the id

    type_cell = pokemon_data_cell.find_all('a', class_='itype')

    sprite = pokemon_image_cell.find('a').find('img')['src']

    if len(type_cell) == 1:
        types = [type_cell[0].text]
    else:
        types = [type_cell[0].text, type_cell[1].text]

    PokemonsData.append(Pokemon(num, name, types, sprite).toDict())

    num += 1

#print(PokemonsData)

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
        types_str = ', '.join(pokemon['types'])
        cursor.execute(insert_query, (pokemon['num'], pokemon['name'], types_str, pokemon['sprite']))
    
    connection.commit()
    print("Data inserted successfully!")

except Exception as error:
    print(f"Error: {error}")

finally:
    cursor.close()
    connection.close()


