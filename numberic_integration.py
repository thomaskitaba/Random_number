#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = e^(-x^2)
def f(x):
    return np.exp(-x**2)

# Monte Carlo method to estimate the integral
def monte_carlo_integration(N):
    # Generate N random samples uniformly distributed in [0, 1]
    x_samples = np.random.uniform(0, 1, N)
    
    # Evaluate the function at the random samples
    function_values = f(x_samples)
    
    # Estimate the integral using the Monte Carlo formula
    integral_estimate = np.mean(function_values)  # Average of the function values
    return integral_estimate

# Set different values for N (number of samples)
N_values = [10**3, 10**4, 10**5, 10**6]
integral_estimates = [monte_carlo_integration(N) for N in N_values]

# Exact value of the integral (numerical integration for comparison)
exact_value = 0.7468241328  # This is the known result of the integral over [0, 1]

# Plot the convergence of the integral estimate as N increases
plt.figure(figsize=(10, 6))
plt.plot(N_values, integral_estimates, label="Monte Carlo Estimate", marker='o')
plt.axhline(y=exact_value, color='r', linestyle='--', label="Exact Value")
plt.xscale('log')
plt.yscale('linear')
plt.xlabel("Number of Samples (N)")
plt.ylabel("Estimated Integral Value")
plt.title("Monte Carlo Estimation of Integral")
plt.legend()
plt.grid(True)
plt.show()

# Print the estimates for each N
for N, estimate in zip(N_values, integral_estimates):
    print(f"Estimated integral with N = {N}: {estimate}")
