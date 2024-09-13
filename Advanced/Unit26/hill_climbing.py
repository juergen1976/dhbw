import numpy as np
import matplotlib.pyplot as plt

# Define the objective function
def f(x):
    return -(x - 3) ** 2 + 10

# Hill Climbing Algorithm
# TODO: Change the step_size and max_iterations to see how the algorithm behaves
# TODO: Change the step_size and max_iterations to see how the algorithm behaves
def hill_climb(initial_x, step_size=0.1, max_iterations=100):
    current_x = initial_x
    current_f = f(current_x)

    for i in range(max_iterations):
        # Move left or right by a small step
        move = np.random.choice([-step_size, step_size])
        new_x = current_x + move
        new_f = f(new_x)

        # If the new solution is better, update
        if new_f > current_f:
            current_x = new_x
            current_f = new_f
            print(f"Iteration {i}: Moving to x = {new_x}, f(x) = {new_f}")
        else:
            print(f"Iteration {i}: No improvement. Stopping.")
            break

    return current_x, current_f

# Initial guess
# TODO: Change the initial guess to see how the algorithm behaves
initial_x = np.random.uniform(-10, 10)
print(f"Starting Hill Climbing from x = {initial_x}")

# Run the hill climbing algorithm
best_x, best_f = hill_climb(initial_x)

print(f"Found maximum at x = {best_x}, f(x) = {best_f}")

# Plotting the function and the result
x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x) = -(x-3)^2 + 10")
plt.scatter(best_x, best_f, color='red', label=f"Maximum at x={best_x:.2f}")
plt.title("Hill Climbing Optimization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
