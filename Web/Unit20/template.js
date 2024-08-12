const apiKey = 'c167fb0ad89756bfe7228cb2e8979dc0';
const apiUrl = 'https://api.openweathermap.org/data/2.5/weather';

class WeatherApp extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = `
            <style>
                /* TODO: Stylings hier hinterlegen */
            </style>
            <div class="container">
                /* TODO: HTML hier hinterlegen */
            </div>
        `;
        this.shadowRoot.getElementById('searchButton').addEventListener('click', () => {
            // TODO Implementierung
        });

        var aktuellButton = this.shadowRoot.getElementById('aktuellButton');
        aktuellButton.addEventListener('click', () => {
            // TODO Implementierung
        });

        this.fetchWeather = this.fetchWeather.bind(this);
        this.fetchLocalWeather = this.fetchLocalWeather.bind(this);
        this.showPosition = this.showPosition.bind(this);
        this.showError = this.showError.bind(this);
    }

    // TODO: Methoden hier implementieren
}
// Define the new element
customElements.define('weather-app', WeatherApp);









