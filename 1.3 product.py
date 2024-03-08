import pandas as pd

def integrate_datasets(orders_df, products_df):
    
    merged_df = pd.merge(orders_df, products_df, on="product_id", how="left")
    
    return merged_df

orders_df = pd.DataFrame({
    'order_id': [1, 2, 3],
    'product_id': [101, 102, 103]
})

products_df = pd.DataFrame({
    'product_id': [101, 102, 103],
    'product_name': ['Product A', 'Product B', 'Product C'],
    'product_price': [10, 20, 30]
})

print("Original orders DataFrame:")
print(orders_df)

print("\nOriginal products DataFrame:")
print(products_df)


merged_df = integrate_datasets(orders_df, products_df)

print("\nMerged DataFrame:")
print(merged_df)
