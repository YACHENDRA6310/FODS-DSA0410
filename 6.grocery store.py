
item_prices = [2.50, 3.00, 1.25]
item_quantities = [5, 3, 2]
discount_rate = 10
tax_rate = 8        
subtotal = sum([price * quantity for price, quantity in zip(item_prices, item_quantities)])
total_discount = subtotal * (discount_rate / 100)
discounted_subtotal = subtotal - total_discount
total_tax = discounted_subtotal * (tax_rate / 100)
final_total_cost = discounted_subtotal + total_tax
print(f"The final total cost for the customer's purchase is: ${final_total_cost:.2f}")
