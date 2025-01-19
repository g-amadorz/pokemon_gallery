import React, { useState } from "react"
import MovieCard from "../components/movie"



function Home(){
    const [searchQuery, setSearchQuery] = useState("");

    const movies = [
        {id:1, title: "Shrek", release_date: "2001"},
        {id:2, title: "Shrek 2", release_date: "2003"},
        {id:3, title: "Shrek 3", release_date: "2007"},
    ];

    const handleSearch = (e) => {
        e.preventDefault()
        alert(searchQuery)
        setSearchQuery(searchQuery)
    };

    return (<div className="home">
            <form onSubmit={handleSearch} className="search-form"> 
                <input 
                type="text" 
                placeholder="Search for movies..." 
                className="search-input"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}>
                </input>
                <button type="submit" className="search-button">
                    Search
                </button>
            </form>
        <div className="movies-grid"> 
            {movies.map
            ((movie) => 
               (
                <MovieCard movie={movie} key={movie.id}/>
                )
                )}
        </div>
    </div>);
}


export default Home;