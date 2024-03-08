import pandas as pd
import matplotlib.pyplot as plt

data = {
    'ProductID': [1, 2, 3, 4, 5],
    'SalesAmount': [5000, 6000, 8000, 12000, 5500],
    'QuantitySold': [100, 120, 90, 150, 80],
    'CustomerID': [101, 102, 103, 104, 105]
}
df = pd.DataFrame(data)

print(df.head())

summary_stats = df.describe()
print("Summary Statistics:")
print(summary_stats)

plt.hist(df['SalesAmount'], bins=20, edgecolor='black')
plt.title('Distribution of SalesAmount')
plt.xlabel('SalesAmount')
plt.ylabel('Frequency')
plt.show()

plt.boxplot(df['SalesAmount'])
plt.title('Boxplot of SalesAmount')
plt.show()

mean_sales = df['SalesAmount'].mean()
variance_sales = df['SalesAmount'].var()
covariance_matrix = df[['SalesAmount', 'QuantitySold']].cov()
print("\nDistribution Analysis:")
print("Mean Sales Amount:", mean_sales)
print("Variance Sales Amount:", variance_sales)

print("\nOutlier Detection:")

print("\nCovariance Matrix:")
print(covariance_matrix)
