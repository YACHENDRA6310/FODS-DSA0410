# Sample user interaction data (number of likes received by each post)
likes_data = [10, 20, 30, 40, 10, 20, 10, 30, 20, 30, 40, 50, 10, 20]

# Initialize an empty dictionary to store the frequency distribution
frequency_distribution = {}

# Iterate over the likes_data list to count the frequency of each number of likes
for likes in likes_data:
    if likes in frequency_distribution:
        frequency_distribution[likes] += 1
    else:
        frequency_distribution[likes] = 1

# Print the frequency distribution
print("Frequency Distribution of Likes:")
for likes, frequency in sorted(frequency_distribution.items()):
    print(f"Likes: {likes}, Frequency: {frequency}")
