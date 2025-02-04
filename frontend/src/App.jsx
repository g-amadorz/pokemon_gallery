import { Routes, Route } from 'react-router-dom';
import './css/App.css';
import NavBar from './components/NavBar';
import NewNavBar from './components/NewNavBar';
import Favourites from './pages/favourites';
import View from './pages/view';

function App() {
  return (
    <div>
      <NavBar/>
      <main className>
        <Routes>
          <Route path ="/" element={<View />}/>
          <Route path ="/favourites" element={<Favourites />}/>
          <Route path=""/>
        </Routes>
      </main>
    </div>
  );
}

export default App;
