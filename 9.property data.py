import numpy as np

# User input for the number of houses
num_houses = int(input("Enter the number of houses: "))

# Initialize an empty list to store house data
house_data_list = []

# Input house data for each house
for i in range(num_houses):
    print(f"\nEnter details for House {i + 1}:")
    bedrooms = int(input("Number of bedrooms: "))
    square_footage = float(input("Square footage: "))
    sale_price = float(input("Sale price: "))
    house_data_list.append([bedrooms, square_footage, sale_price])

# Convert the list of lists into a NumPy array
house_data = np.array(house_data_list)

# Filter the array to select rows with more than four bedrooms
houses_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]  # Assuming bedrooms is the first column

# Extract the sale price column from the filtered array
sale_prices = houses_more_than_4_bedrooms[:, -1]  # Assuming sale price is the last column

# Calculate the average sale price
average_sale_price = np.mean(sale_prices)

print("\nAverage sale price of houses with more than four bedrooms:", average_sale_price)
