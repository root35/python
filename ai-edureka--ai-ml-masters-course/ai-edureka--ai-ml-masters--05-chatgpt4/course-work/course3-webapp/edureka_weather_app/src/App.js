import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import WeatherApp from './WeatherApp';
import Homepage from '../../edureka_weather_app/src/components/Homepage';
import Signup from '../../edureka_weather_app/src/components/Signup';
import Signin from '../../edureka_weather_app/src/components/Signin';
import Weather from '../../edureka_weather_app/src/components/Weather';

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/Homepage">Home</Link>
            </li>
            <li>
              <Link to="/Signup">Signup</Link>
            </li>
            <li>
              <Link to="/Signin">Signin</Link>
            </li>
            <li>
              <Link to="/Weather">Weather</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route exact path="/Homepage" element={<Homepage />} />
          <Route exact path="/Signup" element={<Signup />} />
          <Route exact path="/Signin" element={<Signin />} />
          <Route exact path="/Weather" element={<WeatherApp />} />
        </Routes>

      </div>
    </Router>
  );
};

export default App;
