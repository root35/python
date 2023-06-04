import React, { useState, useEffect } from 'react';
import Weather from './components/Weather';

const API_KEY = '3968876214b937b3f67ff924b0648a68'

const WeatherApp = () => {
  const [weatherData, setWeatherData] = useState(null);
  const [city, setCity] = useState('');

  const fetchWeatherData = async () => {
    try {
      const response = await fetch(
        `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}`

        );
      const data = await response.json();
      setWeatherData(data);
    } catch (error) {
      console.error('Error fetching weather data:', error);
    }
  };

  useEffect(() => {
    if (city) {
      fetchWeatherData();
    }
  }, [city]);

  const handleCityChange = (e) => {
    setCity(e.target.value);
  };

  return (
    <div>
      <h2>Weather App</h2>
      <input type="text" value={city} onChange={handleCityChange} placeholder="Enter city" />
      {weatherData && (
        <Weather
          city={weatherData.city}
          temperature={weatherData.temperature}
          condition={weatherData.condition}
        />
      )}
    </div>
  );
};

export default WeatherApp;
