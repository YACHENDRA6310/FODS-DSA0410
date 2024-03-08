import pandas as pd
import numpy as np
from scipy import stats

# Load the CSV file into a DataFrame
df = pd.read_csv("customer_reviews.csv")

# Assuming 'categories' column contains the product category
# Filter data for the specific product category
specific_category = 'your_specific_category_here'
category_reviews = df[df['categories'] == specific_category]

# Calculate mean rating and standard deviation
mean_rating = category_reviews['reviews rating'].mean()
std_dev = category_reviews['reviews rating'].std()

# Calculate the sample size
n = len(category_reviews)

# Calculate the standard error
se = std_dev / np.sqrt(n)

# Set the confidence level
confidence_level = 0.95

# Calculate the margin of error
margin_of_error = stats.t.ppf((1 + confidence_level) / 2, n - 1) * se

# Calculate the confidence intervals
lower_bound = mean_rating - margin_of_error
upper_bound = mean_rating + margin_of_error

print("Mean rating:", mean_rating)
print("Standard deviation:", std_dev)
print("Sample size:", n)
print("Standard error:", se)
print("Confidence Interval ({}%): [{:.2f}, {:.2f}]".format(confidence_level * 100, lower_bound, upper_bound))
