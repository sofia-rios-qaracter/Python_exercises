# Ask the user for basic data
product_name = str(input("What's the name of the product?: "))
units_sold = int(input("How many units have been sold?: "))
unit_price = float(input("What's the price per unit?: "))

# Print revenue
print(f"So, the total revenue is: {units_sold * unit_price}€")
