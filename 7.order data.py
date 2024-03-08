import pandas as pd

# Input data
order_data = pd.DataFrame({
    'customer_id': [1, 1, 2, 3, 3, 3],
    'order_date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-03'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product B', 'Product C', 'Product A'],
    'order_quantity': [2, 3, 1, 2, 1, 3]
})

# Total number of orders made by each customer
orders_per_customer = order_data.groupby('customer_id').size()

# Average order quantity for each product
avg_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

# Earliest and latest order dates in the dataset
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print("Total number of orders made by each customer:")
print(orders_per_customer)

print("\nAverage order quantity for each product:")
print(avg_order_quantity_per_product)

print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
