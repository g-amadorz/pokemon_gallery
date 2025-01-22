import React, { useEffect, useState } from "react";
import PokemonCard from "../components/PokemonCard";
import "../css/View.css";
import {getPokemon} from '../api';

function View(){
    const [Pokemons, setPokemon] = useState([])
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        const fetchPokemon = async () => {
            try {
            const response = await fetch('http://127.0.0.1:8000/pokemons/all/random')
            const data = await response.json()
            setPokemon(data)
            } catch (err) {
                setError(err)
                console.log("something went wrong")
            }
        };
            fetchPokemon()
                },  
                    []);


    return (
        <div className="view">
            <div className="pokemon-grid">
                {Pokemons.map((p) => (
                    <PokemonCard pokemon={p} key={p.num}/>
                ))}
            </div>
        </div>
    )
}

export default View;