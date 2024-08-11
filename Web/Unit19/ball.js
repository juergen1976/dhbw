const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Set up the canvas size and background color
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
ctx.fillStyle = 'white';
ctx.fillRect(0, 0, canvas.width, canvas.height);

// Define the ball properties
const ballRadius = 20;
const ballColor = 'blue';
let x = canvas.width / 2;
let y = canvas.height - ballRadius;
let dx = (Math.random() * 6) - 3;
let dy = -(Math.random() * 6);

// Function to draw the ball on the canvas
function drawBall() {
  ctx.beginPath();
  ctx.arc(x, y, ballRadius, 0, Math.PI * 2, false);
  ctx.fillStyle = ballColor;
  ctx.fill();
}

// Function to update the ball's position and check for collisions
function updateBall() {
  // Move the ball
  x += dx;
  y += dy;

  // Detect collision with canvas edges
  if (x + ballRadius > canvas.width || x - ballRadius < 0) {
    dx = -dx;
  }
  if (y + ballRadius > canvas.height || y - ballRadius < 0) {
    dy = -dy;
  }

  // Clear the canvas and draw the ball again
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawBall();
}

// Set up the animation loop using requestAnimationFrame
function animate() {
  updateBall();
  requestAnimationFrame(animate);
}

// Start the animation loop
animate();