import "../css/PokemonCard.css";

function PokemonCard({pokemon}) {
    
    
    function onLike(){
        alert("clicked")
    }

    return (
        <div className="pokemon-card">
            <div className="img">
                <img src={pokemon.image} alt={pokemon.name} />
            </div>
            <div className="overlay">
                <div className="name-text">
                    {pokemon.name}
                    <div className="type-text">
                        {pokemon.type}
                    </div>
                        <div className="like-button">
                            <button className='opaque-button' onClick={onLike}>
                                ♥
                            </button>
                        </div>
                </div>
            </div>
        </div>
    );
}

export default PokemonCard;
