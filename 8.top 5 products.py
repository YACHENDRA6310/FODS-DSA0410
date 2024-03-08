import pandas as pd
sales_data = pd.DataFrame({
    'order_date': ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04', '2024-02-05'],
    'product_name': ['Product A', 'Product B', 'Product D', 'Product C', 'Product e'],
    'quantity': [10, 15, 5, 20, 8]
})
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])
start_date = pd.Timestamp.now().replace(day=1) - pd.DateOffset(months=1)
end_date = pd.Timestamp.now().replace(day=1) - pd.DateOffset(days=1)
sales_data_past_month = sales_data[(sales_data['order_date'] >= start_date) & (sales_data['order_date'] <= end_date)]
product_sales_past_month = sales_data_past_month.groupby('product_name')['quantity'].sum()
top_5_products = product_sales_past_month.nlargest(5)
print("Top 5 products sold in the past month:")
print(top_5_products)
