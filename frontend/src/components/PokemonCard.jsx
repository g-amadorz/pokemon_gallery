import "../css/PokemonCard.css";
import { Link } from 'react-router-dom';
import { useParams } from "react-router-dom";

function PokemonCard({pokemon}) {
    const {pokemonName} = useParams(pokemon.name);
    
    function onLike(){
        alert("Clicked!")
    }

    return (
        <div className="pokemon-card">
            <div className="img">
                <img src={pokemon.image} alt={pokemon.name} />
            </div>
            <div className="overlay">
                <div className="name-text">
                    <Link to={`/pokemons/${pokemon.name.toLowerCase()}`}>{pokemon.name}</Link>
                    <div className="type-text">
                        {pokemon.type}
                    </div>
                        <div className="like-button">
                            <button className='opaque-button' onClick={onLike}>
                                Like
                            </button>
                        </div>
                </div>
            </div>
        </div>
    );
}

export default PokemonCard;
