import pandas as pd
def check_data_quality(df):
    missing_values_count = df.isnull().sum().sum()
    duplicates_count = df.duplicated().sum()
    negative_values_count = (df.select_dtypes(include=['int64', 'float64']) < 0).sum().sum()   
    print("Number of missing values:", missing_values_count)
    print("Number of duplicates:", duplicates_count)
    print("Number of negative values:", negative_values_count)
    return {
        'missing_values_count': missing_values_count,
        'duplicates_count': duplicates_count,
        'negative_values_count': negative_values_count
    }
merged_df = pd.DataFrame({
    'order_id': [1, 2, 3],
    'product_id': [101, 102, 103],
    'product_name': ['Product A', 'Product B', None],
    'product_price': [10, 20, None]
})

print("Integrated DataFrame:")
print(merged_df)
data_quality_summary = check_data_quality(merged_df)

print("\nData Quality Summary:")
print(data_quality_summary)
