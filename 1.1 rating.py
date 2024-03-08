import pandas as pd

def clean_rating_column(df, order_column='order_id', product_column='product_id', rating_column='rating', default_value=None):
    for col in [order_column, product_column, rating_column]:
        if col not in df.columns:
            raise ValueError(f"'{col}' column not found in the DataFrame.")

    valid_range = (1, 5)

    df[rating_column] = df[rating_column].apply(lambda x: x if (isinstance(x, (int, float)) and valid_range[0] <= x <= valid_range[1]) else default_value)

    return df

data = {
    'order_id': [1, 2, 3, 4, 5],
    'product_id': [101, 102, 103, 104, 105],
    'rating': [4, 5, 3, 2, 5]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

cleaned_df = clean_rating_column(df, order_column='order_id', product_column='product_id', rating_column='rating', default_value=None)

print("\nCleaned DataFrame:")
print(cleaned_df)
