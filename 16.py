import numpy as np
import matplotlib.pyplot as plt

# Given scores
scores = [85, 78, 92, 89, 67, 76, 94, 82, 91, 88, 75, 81, 96, 90, 79, 83, 77, 85, 98, 72]

# Calculate mean
mean_score = np.mean(scores)

# Calculate median
median_score = np.median(scores)

# Calculate quartiles
first_quartile = np.percentile(scores, 25)
third_quartile = np.percentile(scores, 75)

# Print the results
print("Mean score:", mean_score)
print("Median score:", median_score)
print("First quartile (Q1):", first_quartile)
print("Third quartile (Q3):", third_quartile)


# Create a box plot
plt.boxplot(scores)
plt.title("Box plot of Scores")
plt.ylabel("Score")
plt.show()

# Calculate interquartile range (IQR)
IQR = third_quartile - first_quartile

# Calculate lower and upper bounds for potential outliers
lower_bound = first_quartile - 1.5 * IQR
upper_bound = third_quartile + 1.5 * IQR

# Identify potential outliers
potential_outliers = [score for score in scores if score < lower_bound or score > upper_bound]
print("Potential outliers:", potential_outliers)
