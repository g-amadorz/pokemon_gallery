const BASE_URL = "http://127.0.0.1:8000/pokemons"

export  const getPokemon = async() => {
    const response = await fetch(`${BASE_URL}/3`);
    const data = await response.json()
    return data.results
};