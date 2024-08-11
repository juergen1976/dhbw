document.addEventListener('DOMContentLoaded', function() {
    const gestureBox = document.getElementById('gestureBox');
    let startX, startY, startTime;

    gestureBox.addEventListener('touchstart', function(e) {
        const touch = e.touches[0];
        startX = touch.clientX;
        startY = touch.clientY;
        startTime = new Date().getTime();
    });

    gestureBox.addEventListener('touchend', function(e) {
        const touch = e.changedTouches[0];
        const endX = touch.clientX;
        const endY = touch.clientY;
        const endTime = new Date().getTime();
        const deltaX = endX - startX;
        const deltaY = endY - startY;
        const deltaTime = endTime - startTime;

        // Minimum distance and time threshold to detect a swipe
        const minDistance = 30;
        const maxTime = 700;

        if (deltaTime < maxTime) {
            if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > minDistance) {
                if (deltaX > 0) {
                    gestureBox.textContent = 'Swiped Right';
                } else {
                    gestureBox.textContent = 'Swiped Left';
                }
            } else if (Math.abs(deltaY) > minDistance) {
                if (deltaY > 0) {
                    gestureBox.textContent = 'Swiped Down';
                } else {
                    gestureBox.textContent = 'Swiped Up';
                }
            }
        }
    });
});
