import { Link } from "react-router-dom";
import "../css/navbar.css" 
import { useState } from "react";

function NewNavBar() {
    const  [isOpen, setIsOpen] = useState(false)

    const toggleMenu = () => {
        setIsOpen[!isOpen];
    }
    return <nav className="navbar">
        <div className="navbar-brand">
            <Link to='/'>Poke-Gallery</Link>
        </div>
        <div className="navbar-links">
            <button className="dropdown-toggle" onClick={toggleMenu}>
                Pokemon
            </button>
                    {isOpen && (
                        <ul className="dropdown-menu">
                            <li>
                                <Link to='/'>Pokemon List</Link>
                            </li>
                            <li>
                                <Link to='/pokemon/types'>Pokemon Types</Link>
                            </li>
                            <li>
                                <Link to='/pokemon/abilities'>Pokemon Abilities</Link>
                            </li>
                        </ul>
                    )}
            <div/>
            <Link to='/favourites' className="nav-link">Favourites </Link>
        </div>
    </nav>
}

export default NewNavBar



// return <nav className="navbar">
// <div className="navbar-brand">
//     <Link to='/'>Poke-Gallery</Link>
//     <div className="navbar-links">
//         <div className="dropdown">
//             <button className="dropdown-toggle">
//                 Pokemon
//             </button>
//         </div>
//     </div>
// </div>
// </nav>