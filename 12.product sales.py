import matplotlib.pyplot as plt

# Sample sales data (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1000, 1200, 1500, 1300, 1600, 1800, 2000, 1900, 1700, 1500, 1300, 1100]

# Line plot for sales data
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', color='b', linestyle='-')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1000, 1200, 1500, 1300, 1600, 1800, 2000, 1900, 1700, 1500, 1300, 1100]

# Scatter plot for sales data
plt.figure(figsize=(10, 6))
plt.scatter(months, sales, color='r', marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1000, 1200, 1500, 1300, 1600, 1800, 2000, 1900, 1700, 1500, 1300, 1100]

# Bar plot for sales data
plt.figure(figsize=(10, 6))
plt.bar(months, sales, color='g')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
