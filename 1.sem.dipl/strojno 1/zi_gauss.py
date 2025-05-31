import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for the first Gaussian distribution
mean1 = np.array([2, 2])
covariance1 = np.array([[3.5, -2], [-2, 3.5]])
prior1 = 0.6

# Parameters for the second Gaussian distribution
mean2 = np.array([-3, -7])
covariance2 = np.array([[3.5, -2], [-2, 3.5]])
prior2 = 0.4

# Generate random samples from the two Gaussian distributions
num_samples = 100
samples1 = np.random.multivariate_normal(mean1, covariance1, int(num_samples * prior1))
samples2 = np.random.multivariate_normal(mean2, covariance2, int(num_samples * prior2))

# Create 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the surfaces for the two Gaussian distributions with color intensity based on priors
x, y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
pdf1 = prior1 * multivariate_normal.pdf(np.dstack((x, y)), mean1, covariance1)
pdf2 = prior2 * multivariate_normal.pdf(np.dstack((x, y)), mean2, covariance2)

surface1 = ax.plot_surface(x, y, pdf1, cmap='Reds', alpha=prior1)
surface2 = ax.plot_surface(x, y, pdf2, cmap='Blues', alpha=prior2)

# Calculate the contour line where the densities are equal
contour_line = ax.contour(x, y, pdf1 - pdf2, levels=[0], colors='black', linestyles='dashed')

# Create legends for each class
legend_elements = [
    plt.Line2D([0], [0], color='red', lw=10, label='Class 1'),
    plt.Line2D([0], [0], color='blue', lw=10, label='Class 2'),
    contour_line.collections[0],
]

# Add legend to the plot
ax.legend(handles=legend_elements)

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Probability Density')
ax.set_title('3D Plot of Two Gaussian Distributions with Different Priors')

# Display the plot
plt.show()