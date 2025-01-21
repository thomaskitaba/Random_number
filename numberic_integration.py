#!/usr/bin/python3

import matplotlib.pyplot as plt  # Importing matplotlib for visualization
from matplotlib import gridspec  # Importing gridspec for better layout control
import numpy as np  # Importing numpy for numerical operations

# Initialize variables
MAXN = 10000  # Total number of steps for the numerical integration
n_arr = []  # List to store iteration counts for plotting
pi_arr = []  # List to store π estimates for each iteration

# Set up the plot
fig = plt.figure(figsize=(10, 15))  # Create a figure with specified size
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 1])  # Create a grid layout for subplots (equal space)
ax = [plt.subplot(gs[0]), plt.subplot(gs[1])]  # Define two subplots

# Set limits for both axes to avoid overlap and make sure plots are visible
ax[0].set_xlim(-0.5, 0.5)
ax[0].set_ylim(-0.5, 0.5)
ax[0].set_aspect('equal')  # Ensure equal aspect ratio for square visualization

# Numeric Integration using Trapezoidal Rule
# The function for the quarter circle
def quarter_circle(x):
    return np.sqrt(1 - x**2)

# Approximate pi using the integral of quarter_circle
# Using the trapezoidal rule to numerically integrate
for n in range(1, MAXN + 1):
    # Use the trapezoidal rule to estimate the integral
    x_vals = np.linspace(0, 1, n)  # Generate n points between 0 and 1
    y_vals = quarter_circle(x_vals)  # Evaluate the function at these points
    integral_estimate = np.trapz(y_vals, x_vals)  # Perform trapezoidal integration
    pi_estimate = 4 * integral_estimate  # Multiply by 4 to approximate pi
    
    # Store the current estimate of pi and number of iterations
    n_arr.append(n)
    pi_arr.append(pi_estimate)

# Print final results for reference
print(f"Iterations: {MAXN}, Estimated π: {pi_arr[-1]}")

# Plot results on the second subplot
ax[1].plot(n_arr, pi_arr, "b-", label="Numeric Integration Approximation")  # Plot the π estimates over iterations
ax[1].plot(n_arr, [np.pi] * len(n_arr), "r-", label="Actual π")  # Plot the true value of π for reference
ax[1].legend()  # Add a legend to distinguish between the two lines
ax[1].set_xlabel("Number of Steps")  # Label the x-axis for the second subplot
ax[1].set_ylabel("Estimated π")  # Label the y-axis for the second subplot

# Add titles and finalize the plot
ax[0].set_title("Numeric Integration to Approximate π (Quarter Circle Integration)")  # Title for the first subplot
ax[1].set_title("Convergence of π Estimation Over Steps")  # Title for the second subplot
plt.tight_layout()  # Adjust the layout to prevent overlapping elements
plt.show()  # Display the plot
