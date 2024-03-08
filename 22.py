import numpy as np
from scipy import stats

# Sample scores for two groups of students
group1_scores = np.array([85, 90, 88, 82, 87, 91, 89, 86, 92, 84])
group2_scores = np.array([78, 82, 80, 75, 79, 81, 83, 77, 85, 76])

# Calculate mean scores for each group
mean_group1 = np.mean(group1_scores)
mean_group2 = np.mean(group2_scores)

# Calculate standard deviation for each group
std_dev_group1 = np.std(group1_scores, ddof=1)  # ddof=1 for sample standard deviation
std_dev_group2 = np.std(group2_scores, ddof=1)

# Calculate standard error for each group
se_group1 = std_dev_group1 / np.sqrt(len(group1_scores))
se_group2 = std_dev_group2 / np.sqrt(len(group2_scores))

# Calculate 95% confidence intervals for mean scores
ci_group1 = stats.t.interval(0.95, len(group1_scores) - 1, mean_group1, se_group1)
ci_group2 = stats.t.interval(0.95, len(group2_scores) - 1, mean_group2, se_group2)

print("Group 1 Mean Score:", mean_group1)
print("Group 1 95% Confidence Interval:", ci_group1)
print("Group 2 Mean Score:", mean_group2)
print("Group 2 95% Confidence Interval:", ci_group2)

# Perform hypothesis test
t_stat, p_value = stats.ttest_ind(group1_scores, group2_scores)

alpha = 0.05
if p_value < alpha:
    print("Reject null hypothesis. There is a significant difference between the two groups.")
else:
    print("Fail to reject null hypothesis. There is no significant difference between the two groups.")
