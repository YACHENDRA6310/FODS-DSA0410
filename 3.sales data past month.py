import numpy as np
sales_data = np.array([[100, 150, 200], [120, 130, 160], [80, 90, 110]])
average_price = np.mean(sales_data, axis=1)
print("Average price for each product:")
for i, avg_price in enumerate(average_price):
    print(f"Product {i+1}: ${avg_price:.2f}")
