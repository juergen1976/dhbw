const battery = navigator.battery || navigator.webkitBattery;

if (battery) {
  const levelElement = document.getElementById('batteryLevel');
  const statusElement = document.getElementById('chargingStatus');

  // Update the battery level and charging status every second
  setInterval(() => {
    levelElement.textContent = `${battery.level * 100}%`;
    statusElement.textContent = `${battery.charging ? 'Charging' : 'Not Charging'}`;
  }, 1000);

  // Display the initial battery level and charging status
  levelElement.textContent = `${battery.level * 100}%`;
  statusElement.textContent = `${battery.charging ? 'Charging' : 'Not Charging'}`;

  // Listen for changes in the battery level and charging status
  battery.onlevelchange = () => {
    levelElement.textContent = `${battery.level * 100}%`;
  };

  battery.onchargingchange = () => {
    statusElement.textContent = `${battery.charging ? 'Charging' : 'Not Charging'}`;
  };
} else {
  console.error('Battery Status API is not supported in this browser.');
}