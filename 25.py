import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Data from the clinical trial
placebo_group = np.array([5, 8, 6, 4, 7, 3, 5, 4, 6, 7])
treatment_group = np.array([10, 12, 11, 9, 13, 11, 10, 12, 14, 13])

# Perform hypothesis test
t_stat, p_value = stats.ttest_ind(placebo_group, treatment_group)

alpha = 0.05
if p_value < alpha:
    print("Reject null hypothesis. The new treatment has a statistically significant effect compared to the placebo.")
else:
    print("Fail to reject null hypothesis. There is no statistically significant effect of the new treatment compared to the placebo.")

# Visualize the data and p-value
plt.bar(['Placebo', 'Treatment'], [np.mean(placebo_group), np.mean(treatment_group)], yerr=[np.std(placebo_group), np.std(treatment_group)], capsize=5)
plt.ylabel('Mean Effect')
plt.title('Effectiveness of Placebo vs Treatment')
plt.text(0, np.mean(placebo_group) + 0.5, f'Mean: {np.mean(placebo_group):.2f}\nStd: {np.std(placebo_group):.2f}', ha='center')
plt.text(1, np.mean(treatment_group) + 0.5, f'Mean: {np.mean(treatment_group):.2f}\nStd: {np.std(treatment_group):.2f}', ha='center')
plt.axhline(y=np.mean(placebo_group), color='gray', linestyle='--')
plt.axhline(y=np.mean(treatment_group), color='gray', linestyle='--')
plt.text(0.5, max(np.mean(placebo_group), np.mean(treatment_group)) + 0.5, f'p-value: {p_value:.4f}', ha='center')
plt.show()
