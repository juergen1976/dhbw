import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance


# Step 1: Generate random points
def generate_random_points(num_points):
    return np.random.rand(num_points, 2)  # Points in 2D space


# Step 2: Find the closest pair
def find_closest_pair(points):
    dist_matrix = distance.cdist(points, points)  # Compute distance matrix
    np.fill_diagonal(dist_matrix, np.inf)  # Exclude diagonal (same point comparisons)
    min_dist = np.min(dist_matrix)
    min_index = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)
    return min_dist, min_index


# Step 3: Visualize the points and closest pair
def plot_points(points, closest_pair_indices):
    plt.figure(figsize=(8, 6))
    plt.scatter(points[:, 0], points[:, 1], color='blue', label='Points')

    # Plot closest pair
    if closest_pair_indices:
        p1, p2 = points[closest_pair_indices[0]], points[closest_pair_indices[1]]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'ro-', label='Closest Pair', markersize=10)
        plt.text((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2, f'{np.linalg.norm(p2 - p1):.2f}',
                 fontsize=12, color='red', ha='center')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Random Points and Closest Pair')
    plt.legend()
    plt.grid(True)
    plt.show()


# Main execution
num_points = 20  # Number of random points
points = generate_random_points(num_points)
closest_distance, closest_pair = find_closest_pair(points)
print(f'Closest pair distance: {closest_distance}')
print(f'Closest pair indices: {closest_pair}')

plot_points(points, closest_pair)
