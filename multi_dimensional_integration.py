#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_integral_2d(f, a, b, N):
    """
    Estimate the integral of a 2D function f(x, y) over [a, b] x [a, b] using Monte Carlo method.
    
    Parameters:
    f  : function : The function to integrate.
    a  : float    : Lower bound of integration.
    b  : float    : Upper bound of integration.
    N  : int      : Number of random samples.
    
    Returns:
    float : Estimated integral.
    """
    # Generate random samples in the 2D space [a, b] x [a, b]
    x_samples = np.random.uniform(a, b, N)
    y_samples = np.random.uniform(a, b, N)
    
    # Compute the function values at the random samples
    f_values = f(x_samples, y_samples)
    
    # Compute the Monte Carlo estimate for the 2D integral
    integral_estimate = (b - a) * (b - a) * np.mean(f_values)
    
    return integral_estimate

# Define the 2D function e^{-(x^2 + y^2)}
def f_2d(x, y):
    return np.exp(-(x**2 + y**2))

# Estimate the 2D integral for different N values
N_values = [10**3, 10**4, 10**5, 10**6]
integral_2d_estimates = [monte_carlo_integral_2d(f_2d, 0, 1, N) for N in N_values]

# Print the 2D integral estimates
for N, estimate in zip(N_values, integral_2d_estimates):
    print(f"N = {N}, Estimated 2D Integral = {estimate}")

# Plot the estimates for different N values
plt.figure(figsize=(8, 6))
plt.plot(N_values, integral_2d_estimates, marker='o', linestyle='-', color='b')
plt.xscale('log')
plt.yscale('linear')
plt.xlabel('Number of samples (N)')
plt.ylabel('Estimated Integral')
plt.title('Monte Carlo Estimate of 2D Integral for Different N Values')
plt.grid(True)
plt.show()
