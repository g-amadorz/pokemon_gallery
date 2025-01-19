import { Link } from "react-router-dom";


function NavBar() {
    return <nav className="navbar">
        <div className="navbar-brand">
            <Link to='/'>Poke-Gallery</Link>
        </div>
        <div className="navbar-links">
            <Link to='/' className="nav-link">Pokemon</Link>
            <div/>
            <Link to='/favourites' className="nav-link">Favourites </Link>
        </div>
    </nav>
}

export default NavBar