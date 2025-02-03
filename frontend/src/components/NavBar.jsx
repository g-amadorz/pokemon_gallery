import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function NavBar() {
    const [isOpen, setIsOpen] = useState(false);

    const toggleMenu = () => {
        setIsOpen(!isOpen);
    };

    return (
        <nav className="navbar">
            <div className="navbar-links">
                <div className="dropdown">
                    <button className="dropdown-toggle" onClick={toggleMenu}>
                        Pokémon
                    </button>
                    {isOpen && (
                        <ul className="dropdown-menu">
                            <li>
                                <Link to='/' className="dropdown-link">Pokemon List</Link>
                            </li>
                            <li>
                                <Link to='/pokemon/types' className="dropdown-link">Pokémon Types</Link>
                            </li>
                            <li>
                                <Link to='/pokemon/abilities' className="dropdown-link">Pokemon Abilities</Link>
                            </li>
                        </ul>
                    )}
                </div>
                <Link to='/favourites' className="nav-link">Favourites</Link>
            </div>
        </nav>
    );
}

export default NavBar;