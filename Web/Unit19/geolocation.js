
function showTemperature(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;

  // Make an API request to OpenWeatherMap to get the current temperature
  const apiKey = 'c167fb0ad89756bfe7228cb2e8979dc0';
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;
  
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const temperature = data.main.temp;
      const tempElement = document.getElementById('temperature');
      tempElement.textContent = `${temperature}°C`;
    })
    .catch(error => console.error(error));
}

navigator.geolocation.getCurrentPosition(showTemperature);
