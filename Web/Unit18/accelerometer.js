if ('Accelerometer' in window) {
    const accelerometer = new Accelerometer({frequency: 60});

    accelerometer.addEventListener('reading', () => {
        console.log(`X: ${accelerometer.x.toFixed(2)}, Y: ${accelerometer.y.toFixed(2)}, Z: ${accelerometer.z.toFixed(2)}`);
        document.getElementById('output').innerText = 
        `X: ${accelerometer.x.toFixed(2)}, Y: ${accelerometer.y.toFixed(2)}, Z: ${accelerometer.z.toFixed(2)}`;
    });

    accelerometer.addEventListener('error', (event) => {
        console.error(`Accelerometer error: ${event.error.name}`);
    });

    accelerometer.start();
} else {
    document.getElementById('output').innerText = 'Accelerometer API not supported on this device.';
}
