const apiKey = 'c167fb0ad89756bfe7228cb2e8979dc0';
const apiUrl = 'https://api.openweathermap.org/data/2.5/weather';

class WeatherApp extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = `
            <style>
                /* Stylings hier hinterlegen */
            </style>
            <div class="container">
                /* HTML hier hinterlegen */
            </div>
        `;
        this.shadowRoot.getElementById('searchButton').addEventListener('click', () => {
            // Implementierung
        });

        var aktuellButton = this.shadowRoot.getElementById('aktuellButton');
        aktuellButton.addEventListener('click', () => {
            // Implementierung
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









