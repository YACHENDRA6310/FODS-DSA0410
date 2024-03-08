import numpy as np
from scipy import stats

# Conversion rate data for website design A and B
design_A_conversion = np.array([0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0])
design_B_conversion = np.array([1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1])

# Calculate conversion rates for each design
conversion_rate_A = np.mean(design_A_conversion)
conversion_rate_B = np.mean(design_B_conversion)

# Perform hypothesis test to determine if there's a significant difference
t_stat, p_value = stats.ttest_ind(design_A_conversion, design_B_conversion)

alpha = 0.05
if p_value < alpha:
    print("Reject null hypothesis. There is a statistically significant difference in mean conversion rates.")
else:
    print("Fail to reject null hypothesis. There is no statistically significant difference in mean conversion rates.")

print("Conversion rate for Design A:", conversion_rate_A)
print("Conversion rate for Design B:", conversion_rate_B)
