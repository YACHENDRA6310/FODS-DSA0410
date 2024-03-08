import pandas as pd

def handle_missing_values(df):

    for col in df.columns:
        if df[col].dtype == 'object':
            
            mode_value = df[col].mode()[0]
            df[col] = df[col].fillna(mode_value)
        elif df[col].dtype in ['int64', 'float64']:
            
            mean_value = df[col].mean()
            df[col] = df[col].fillna(mean_value)
    
    return df


merged_df = pd.DataFrame({
    'order_id': [1, 2, 3],
    'product_id': [101, 102, 103],
    'product_name': ['Product A', 'Product B', None],
    'product_price': [10, 20, None]
})

print("Original DataFrame:")
print(merged_df)


merged_df = handle_missing_values(merged_df)

print("\nDataFrame with missing values handled:")
print(merged_df)
