from getters import get_float, get_int, get_str

product_name = get_str("What's the name of the product?: ", "Please enter a valid product name.")
units_sold = get_int("How many units have been sold?: ", "Please enter a valid number of units.")
unit_price = get_float("What's the price per unit?: ", "Please enter a valid price")
active_product = bool(input("Is it active? 0 for no, 1 for yes: "))

print(active_product)

# Calculate total sales
total_sales = units_sold * unit_price

print(f"So your sales are: {total_sales}")

if total_sales >= 2000 and active_product: 
    performance = "High performance"
elif total_sales >= 1000:
    performance = "Medium performance"
else:
    performance = "Low performance"

print(f"Your product have a {performance.lower()}")