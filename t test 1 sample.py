import numpy as np
import scipy.stats as stats
import seaborn as sns

# Load the full Iris dataset (considered as the population)
iris = sns.load_dataset("iris")

# Extract Sepal Length as the population data
population_data = iris["sepal_length"]

# Estimate "Population" Parameters
population_mean = np.mean(population_data)

# Take a Random Sample (Simulating a Real-World Sample)
np.random.seed(42)  # For reproducibility
sample_size = 30
sample = np.random.choice(population_data, sample_size, replace=False)

# Compute Sample Mean & Standard Deviation
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)  # Use ddof=1 for sample standard deviation

# Perform One-Sample t-Test
t_statistic, p_value = stats.ttest_1samp(sample, population_mean)

# Print Results
print(f"Estimated Population Mean: {population_mean:.2f}")
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Sample Std Dev: {sample_std:.2f}")
print(f"T-Statistic: {t_statistic:.2f}")
print(f"P-Value: {p_value:.4f}")

# Decision
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The sample mean is significantly different.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")
