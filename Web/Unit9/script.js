const apiKey = 'c167fb0ad89756bfe7228cb2e8979dc0';
const apiUrl = 'https://api.openweathermap.org/data/2.5/weather';

const locationInput = document.getElementById('locationInput');
const searchButton = document.getElementById('searchButton');
const aktuellButton = document.getElementById('aktuellButton');
const locationElement = document.getElementById('location');
const temperatureElement = document.getElementById('temperature');
const descriptionElement = document.getElementById('description');

searchButton.addEventListener('click', () => {
    const location = locationInput.value;
    if (location) {
        fetchWeather(location);
    }
});


function fetchWeather(location) {
    const url = `${apiUrl}?q=${location}&appid=${apiKey}&units=metric`;

    //  set cursor to wait
    searchButton.style.cursor = 'wait';
    searchButton.disabled = true;
    
    fetch(url)
        .then(response => response.json())
        .then(jsonData => {
            locationElement.textContent = jsonData.name;
            temperatureElement.textContent = `${Math.round(jsonData.main.temp)}°C`;
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

aktuellButton.addEventListener('click', () => {
    //  set cursor to wait
    aktuellButton.style.cursor = 'wait';
    aktuellButton.disabled = true;

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
            locationElement.textContent = data.name;
            temperatureElement.textContent = `${Math.round(data.main.temp)}°C`;
            descriptionElement.textContent = data.weather[0].description;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
        })
        .finally(() => {
            aktuellButton.style.cursor = 'pointer';
            aktuellButton.disabled = false;
        });
}