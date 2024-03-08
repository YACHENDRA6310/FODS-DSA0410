import numpy as np
from scipy import stats

# Lifespan data for two product types
product1_lifespans = np.array([50, 55, 60, 65, 70])
product2_lifespans = np.array([45, 50, 55, 60, 65, 70, 75])

# Calculate point estimates for the mean lifespan of each product type
mean_product1 = np.mean(product1_lifespans)
mean_product2 = np.mean(product2_lifespans)

# Calculate standard deviation for each product type
std_dev_product1 = np.std(product1_lifespans, ddof=1)  # ddof=1 for sample standard deviation
std_dev_product2 = np.std(product2_lifespans, ddof=1)

# Calculate standard error for each product type
se_product1 = std_dev_product1 / np.sqrt(len(product1_lifespans))
se_product2 = std_dev_product2 / np.sqrt(len(product2_lifespans))

# Construct 90% confidence intervals for the mean lifespans
ci_product1 = stats.t.interval(0.90, len(product1_lifespans) - 1, mean_product1, se_product1)
ci_product2 = stats.t.interval(0.90, len(product2_lifespans) - 1, mean_product2, se_product2)

print("Product 1 Mean Lifespan:", mean_product1)
print("Product 1 90% Confidence Interval:", ci_product1)
print("Product 2 Mean Lifespan:", mean_product2)
print("Product 2 90% Confidence Interval:", ci_product2)

# Perform hypothesis test to assess if there's a significant difference in lifespans
t_stat, p_value = stats.ttest_ind(product1_lifespans, product2_lifespans)

alpha = 0.05
if p_value < alpha:
    print("Reject null hypothesis. There is a statistically significant difference in lifespans.")
else:
    print("Fail to reject null hypothesis. There is no statistically significant difference in lifespans.")
