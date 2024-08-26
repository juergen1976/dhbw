// Define a class for the custom element
class SimpleCounter extends HTMLElement {
    constructor() {
        super(); // Always call super() first in the constructor.
        // Attach a shadow DOM tree to the instance of the custom element
        this.attachShadow({ mode: 'open' });

        // Set initial state
        this.count = 0;

        // Create elements
        const container = document.createElement('div');
        const countDisplay = document.createElement('span');
        const incrementButton = document.createElement('button');

        // Set text content
        countDisplay.textContent = this.count;
        incrementButton.textContent = 'Increment';

        // Add styles
        const style = document.createElement('style');
        style.textContent = `
            div {
                display: flex;
                align-items: center;
                font-family: Arial, sans-serif;
                background-color: #f3f3f3;
                padding: 10px;
                border-radius: 5px;
                width: 200px;
                justify-content: space-between;
            }
            button {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        `;

        // Append elements to the shadow DOM
        container.appendChild(countDisplay);
        container.appendChild(incrementButton);
        this.shadowRoot.append(style, container);

        // Event listener to handle incrementing
        incrementButton.addEventListener('click', () => {
            this.count++;
            countDisplay.textContent = this.count;
        });
    }
}

// Define the new element
// TODO: über customElements.define() simple-counter als benutzerdefiniertes Element registrieren
