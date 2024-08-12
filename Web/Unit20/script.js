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
        this.shadowRoot.getElementById('searchButton').addEventListener('click', () => {
            const location = this.shadowRoot.getElementById('locationInput').value;
            if (location) {
                this.fetchWeather(location);
            }
        });

        var aktuellButton = this.shadowRoot.getElementById('aktuellButton');
        aktuellButton.addEventListener('click', () => {
            //  set cursor to wait
            aktuellButton.style.cursor = 'wait';
            aktuellButton.disabled = true;
        
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(this.showPosition, this.showError);
            } else {
                document.getElementById('weatherData').innerHTML = "Geolocation is not supported by this browser.";
            }
        });

        this.fetchWeather = this.fetchWeather.bind(this);
        this.fetchLocalWeather = this.fetchLocalWeather.bind(this);
        this.showPosition = this.showPosition.bind(this);
        this.showError = this.showError.bind(this);
    }

    fetchWeather(location) {
        const url = `${apiUrl}?q=${location}&appid=${apiKey}&units=metric`;
        var searchButton = this.shadowRoot.getElementById('searchButton');
        var locationElement = this.shadowRoot.getElementById('location');
        var temperatureElement = this.shadowRoot.getElementById('temperature');
    
        //  set cursor to wait
        searchButton.style.cursor = 'wait';
        searchButton.disabled = true;
        
        fetch(url)
            .then(response => response.json())
            .then(jsonData => {
                locationElement.innerText = jsonData.name;
                temperatureElement.innerText = `${Math.round(jsonData.main.temp)}°C`;
            })
            .catch(error => {
                console.error('Error fetching weather data:', error);
            })
            .finally(() => {
                searchButton.style.cursor = 'pointer';
                searchButton.disabled  = false;
            });
    }
    
    
    // Aktuelle Position mittels Geolocation API
    showError(error) {
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
    
    fetchLocalWeather(lat, lon) {
        const url = `${apiUrl}?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;
        var locationElement = this.shadowRoot.getElementById('location');
        var temperatureElement = this.shadowRoot.getElementById('temperature');
        var descriptionElement = this.shadowRoot.getElementById('description');
        var aktuellButton = this.shadowRoot.getElementById('aktuellButton');
    
        fetch(url)
            .then(response => response.json())
            .then(data => {
                locationElement.innerText = data.name;
                temperatureElement.innerText = `${Math.round(data.main.temp)}°C`;
                descriptionElement.innerText = data.weather[0].description;
            })
            .catch(error => {
                console.error('Error fetching weather data:', error);
            })
            .finally(() => {
                aktuellButton.style.cursor = 'pointer';
                aktuellButton.disabled = false;
            });
    }

    showPosition(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        this.fetchLocalWeather(lat, lon);
    }

}

// Define the new element and get it
customElements.define('weather-app', WeatherApp);
const weatherApp = document.querySelector('weather-app');









