import numpy as np

# Assume your sales data is stored in a 3x3 NumPy array called 'house_data'
house_data = np.array([[3, 1500, 200000], [4, 1800, 250000], [5, 2000, 300000], [6, 2200, 350000], [4, 1900, 270000], [5, 2100, 320000]])

# Filter rows with more than four bedrooms
filtered_data = house_data[house_data[:, 0] > 4]

# Calculate the mean of the sale prices for the filtered rows
average_sale_price = np.mean(filtered_data[:, 2])  # Assuming the sale price is in the third column

print(f"The average sale price of houses with more than four bedrooms is: {average_sale_price:.2f}")
