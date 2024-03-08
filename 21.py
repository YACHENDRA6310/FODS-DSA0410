import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Create a DataFrame with age and body fat data
data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    'body_fat_percent': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}
df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation of age and %fat
age_mean = df['age'].mean()
age_median = df['age'].median()
age_std = df['age'].std()

fat_mean = df['body_fat_percent'].mean()
fat_median = df['body_fat_percent'].median()
fat_std = df['body_fat_percent'].std()

print("Age statistics:")
print("Mean:", age_mean)
print("Median:", age_median)
print("Standard Deviation:", age_std)

print("\nBody Fat Percentage statistics:")
print("Mean:", fat_mean)
print("Median:", fat_median)
print("Standard Deviation:", fat_std)

# Draw boxplots for age and %fat
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.boxplot(df['age'])
plt.title('Boxplot of Age')
plt.ylabel('Age')

plt.subplot(1, 2, 2)
plt.boxplot(df['body_fat_percent'])
plt.title('Boxplot of Body Fat Percentage')
plt.ylabel('Body Fat Percentage')

plt.tight_layout()
plt.show()

# Draw scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['body_fat_percent'])
plt.title('Scatter Plot of Age vs. Body Fat Percentage')
plt.xlabel('Age')
plt.ylabel('Body Fat Percentage')
plt.grid(True)
plt.show()

# Draw q-q plot
plt.figure(figsize=(8, 6))
stats.probplot(df['age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
stats.probplot(df['body_fat_percent'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Body Fat Percentage')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.grid(True)
plt.show()
