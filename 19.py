from collections import Counter

# Sample purchase amounts data
purchase_amounts = [50, 60, 70, 50, 80, 90, 70, 60, 50, 80, 50, 70, 80, 90]

# Calculate the mean (average) purchase amount
mean_purchase_amount = sum(purchase_amounts) / len(purchase_amounts)

# Identify the mode (most frequently occurring purchase amount)
purchase_amount_counts = Counter(purchase_amounts)
mode_purchase_amount = purchase_amount_counts.most_common(1)[0][0]

# Print the results
print("Mean purchase amount:", mean_purchase_amount)
print("Mode purchase amount:", mode_purchase_amount)
