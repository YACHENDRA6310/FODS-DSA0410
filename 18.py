# Sample weather data (weather conditions and their frequencies)
weather_data = {
    'Sunny': 50,
    'Cloudy': 30,
    'Rainy': 20,
    'Snowy': 10
}

# Initialize variables to track the most common weather type
max_frequency = 0
most_common_weather = None

# Calculate the frequency distribution and find the most common weather type
for weather, frequency in weather_data.items():
    print(f"{weather}: {frequency} occurrences")
    if frequency > max_frequency:
        max_frequency = frequency
        most_common_weather = weather

# Print the most common weather type
print("\nThe most common weather type is:", most_common_weather)
