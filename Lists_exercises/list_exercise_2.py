order_quantities = [1, 3, 5, 2, 6, 4, 1]
more_than_3 = 0

for orders in order_quantities:
    if orders > 3:
        more_than_3 += 1

print(f"There are a total of {len(order_quantities)} orders")
print(f"There were {more_than_3} orders with more than 3 items")