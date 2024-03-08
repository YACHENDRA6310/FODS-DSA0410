import pandas as pd

customer_demographics_data = {
    'customer_id': [1, 2, 3, 4, 5],
    'age': [25, 35, 30, 45, 28],
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'location': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'San Francisco']
}

customer_demographics_df = pd.DataFrame(customer_demographics_data)

user_activity_logs_data = {
    'customer_id': [1, None, 3, 4, 5],
    'timestamp': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'page_views': [100, 120, 80, None, 90],
    'interaction_duration': [30, 40, 25, 50, 35]
}

user_activity_logs_df = pd.DataFrame(user_activity_logs_data)

customer_support_data = {
    'customer_id': [1, 2, 3, 4, 5],
    'support_tickets': [2, 1, 3, 2, 1],
    'satisfaction_score': [4, 5, 3, 4, None]
}

customer_support_df = pd.DataFrame(customer_support_data)

customer_support_df = customer_support_df.dropna(subset=['satisfaction_score'])


merged_df = pd.merge(customer_demographics_df, user_activity_logs_df, on='customer_id', how='left')
merged_df = pd.merge(merged_df, customer_support_df, on='customer_id', how='left')

resultant_df=merged_df.dropna()



resultant_df.to_csv('resultant_dataset.csv', index=False)

print(resultant_df.to_string(index=False))

