import pandas as pd

data = {
    'customer_id' : [1, 2, 3, 4, 5],
    'product_id' : [100, 101, 102, 103, 104],
    'rating'  : [4, 5, 2, 'invalid', 3],
    'review' : ['great', 'superb', 'must buy', 'worst', 'notgood'],
    'order_date': ['2023-05-15', '2023-06-20', '2023-07-10', '2023-08-05', '2023-09-18']
}


df_orders = pd.DataFrame(data)

def transform_order_date(df, date_column='order_date'):
    try:
        
        df[date_column] = pd.to_datetime(df[date_column])

       
        df['month'] = df[date_column].dt.month

        return df
    except Exception as e:
        print("Error occurred during date transformation:", e)
        return None


transformed_orders = transform_order_date(df_orders)


print("Transformed DataFrame:")
print(transformed_orders)
