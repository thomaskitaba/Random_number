#!/usr/bin/python3
import matplotlib.pyplot as plt  # Importing matplotlib for visualization
from matplotlib import gridspec  # Importing gridspec for better layout control
import numpy as np  # Importing numpy for numerical operations

# Initialize variables
MAXN = 10000  # Total number of iterations for the simulation
n = 1  # Current iteration number
n_circle = 0  # Counter for points inside the circle
n_arr = []  # List to store iteration counts for plotting
pi_arr = []  # List to store π estimates for each iteration
error_arr = []  # List to store error values for each iteration

# Set up the plot with three subplots (including error analysis)
fig = plt.figure(figsize=(10, 20))  # Create a figure with specified size
gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 1])  # Create a grid layout for three subplots
ax = [plt.subplot(gs[0]), plt.subplot(gs[1]), plt.subplot(gs[2])]  # Define three subplots
circle = plt.Circle((0, 0), radius=0.5, fc='y', alpha=0.3)  # Create a visual representation of the circle
ax[0].add_patch(circle)  # Add the circle to the first subplot

# Set limits for the first subplot
ax[0].set_xlim(-0.5, 0.5)
ax[0].set_ylim(-0.5, 0.5)
ax[0].set_aspect('equal')  # Ensure equal aspect ratio for square visualization

# Monte Carlo simulation
while n <= MAXN:  # Loop until the maximum number of iterations is reached
    x, y = np.random.uniform(-0.5, 0.5, 2)  # Generate a random point (x, y) within the square
    color = 'b'  # Default color for points outside the circle

    if x**2 + y**2 <= 0.25:  # Check if the point is inside the circle (distance from origin ≤ radius)
        n_circle += 1  # Increment the counter for points inside the circle
        color = 'r'  # Change color to red for points inside the circle

    ax[0].plot(x, y, color + '+', markersize=1)  # Plot the point on the first subplot
    n_arr.append(n)  # Record the current iteration number
    pi_estimate = 4 * n_circle / n  # Calculate the approximation of π
    pi_arr.append(pi_estimate)  # Store the π estimate
    error_arr.append(abs(np.pi - pi_estimate))  # Compute and store the absolute error
    n += 1  # Increment the iteration counter

# Print final results for reference
print(f"Iterations: {n-1}, Points in Circle: {n_circle}, Estimated π: {pi_arr[-1]}")

# Plot results on the second subplot
ax[1].plot(n_arr, pi_arr, "b-", label="Monte Carlo Approximation")  # Plot the π estimates over iterations
ax[1].plot(n_arr, [np.pi] * len(n_arr), "r-", label="Actual π")  # Plot the true value of π for reference
ax[1].legend()  # Add a legend to distinguish between the two lines
ax[1].set_xlabel("Number of Iterations")  # Label the x-axis for the second subplot
ax[1].set_ylabel("Estimated π")  # Label the y-axis for the second subplot

# Plot the error analysis on the third subplot
ax[2].plot(n_arr, error_arr, "g-", label="Error |π_estimated - π_actual|")  # Plot the absolute error
ax[2].legend()  # Add a legend to distinguish the error plot
ax[2].set_xlabel("Number of Iterations")  # Label the x-axis for the third subplot
ax[2].set_ylabel("Absolute Error")  # Label the y-axis for the third subplot
ax[2].set_title("Error Analysis: Absolute Error in π Estimation")  # Title for the error plot

# Add titles to the first two subplots
ax[0].set_title("Monte Carlo Approximation of π (Points in Circle vs. Square)")  # Title for the first subplot
ax[1].set_title("Convergence of π Estimation Over Iterations")  # Title for the second subplot

# Adjust layout and display
plt.tight_layout()  # Adjust the layout to prevent overlapping elements
plt.show()  # Display the plot
