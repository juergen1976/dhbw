const apiKey = 'c167fb0ad89756bfe7228cb2e8979dc0';
const apiUrl = 'https://api.openweathermap.org/data/2.5/weather';

class WeatherApp extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = `
            <style>
                .container {
                    max-width: 400px;
                    margin: 0 auto;
                    text-align: center;
                    padding: 20px;
                    background-color: rgba(255, 255, 255, 0.5); /* Set the background color to be transparent */
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); /* Adjust the alpha value here for the box shadow transparency */
                    margin-top: 105px;
                }
                h1 {
                    font-size: 24px;
                }

                input[type="text"] {
                    width: 90%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                button {
                    background-color: #1c1cd8;
                    color: #fff;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .weather-info {
                    margin-top: 20px;
                }
            </style>
            <div class="container">
                <h1>DHBW Wetter App</h1>
                <input type="text" id="locationInput" placeholder="Geben sie eine Stadt ein...">
                <button id="searchButton">Suchen</button>
                <button id="aktuellButton">Standort</button>
                <div class="weather-info">
                    <h2 id="location"></h2>
                    <p id="temperature"></p>
                    <p id="description"></p>
                </div>
            </div>
        `;
    }

    // Getter and setter for location input
    get locationInput() {
        return this.shadowRoot.getElementById('locationInput').value;
    }

    set locationInput(value) {
        this.shadowRoot.getElementById('locationInput').value = value;
    }

    // Getter and setter for location display
    get location() {
        return this.shadowRoot.getElementById('location').innerText;
    }

    set location(value) {
        this.shadowRoot.getElementById('location').innerText = value;
    }

    // Getter and setter for temperature display
    get temperature() {
        return this.shadowRoot.getElementById('temperature').innerText;
    }

    set temperature(value) {
        this.shadowRoot.getElementById('temperature').innerText = value;
    }

    // Getter and setter for description display
    get description() {
        return this.shadowRoot.getElementById('description').innerText;
    }

    set description(value) {
        this.shadowRoot.getElementById('description').innerText = value;
    }

    // Access buttons directly if needed
    get searchButton() {
        return this.shadowRoot.getElementById('searchButton');
    }

    get aktuellButton() {
        return this.shadowRoot.getElementById('aktuellButton');
    }
}

// Define the new element
customElements.define('weather-app', WeatherApp);

const weatherApp = document.querySelector('weather-app');


weatherApp.searchButton.addEventListener('click', () => {
    const location = weatherApp.locationInput;
    if (location) {
        fetchWeather(location);
    }
});


function fetchWeather(location) {
    const url = `${apiUrl}?q=${location}&appid=${apiKey}&units=metric`;

    //  set cursor to wait
    weatherApp.searchButton.style.cursor = 'wait';
    weatherApp.searchButton.disabled = true;
    
    fetch(url)
        .then(response => response.json())
        .then(jsonData => {
            weatherApp.location = jsonData.name;
            weatherApp.temperature = `${Math.round(jsonData.main.temp)}°C`;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
        })
        .finally(() => {
            weatherApp.temperature = `${Math.round(jsonData.main.temp)}°C`;
            weatherApp.searchButton.style.cursor = 'pointer';
            weatherApp.searchButton.disabled  = false;
        });
}


// Aktuelle Position mittels Geolocation API
function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}

function showPosition(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    fetchLocalWeather(lat, lon);
}

weatherApp.aktuellButton.addEventListener('click', () => {
    //  set cursor to wait
    weatherApp.aktuellButton.style.cursor = 'wait';
    weatherApp.aktuellButton.disabled = true;

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        document.getElementById('weatherData').innerHTML = "Geolocation is not supported by this browser.";
    }
});

function fetchLocalWeather(lat, lon) {
    const url = `${apiUrl}?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            weatherApp.location = data.name;
            weatherApp.temperature = `${Math.round(data.main.temp)}°C`;
            weatherApp.description = data.weather[0].description;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
        })
        .finally(() => {
            weatherApp.aktuellButton.style.cursor = 'pointer';
            weatherApp.aktuellButton.disabled = false;
        });
}