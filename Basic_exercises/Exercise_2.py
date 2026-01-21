from getters import get_float, get_int, get_str

# Asking the user for the data
customer_name = get_str("Enter the customer's name: ", "Please enter a valid name.")
age = get_int("Enter the customer's age: ", "Please enter a valid age.")
monthly_spending = get_float("Enter the customer's monthly spending: ", "Please enter a valid amount.")

# Determines wether the customer is an adult or a minor
if age >= 18:
    age_status = "adult"
else:
    age_status = "minor"
    if monthly_spending > 500:
        print("HOW?? I wish I have your parents")

if monthly_spending >= 1000:
    category = "Premium"
elif monthly_spending >= 500:
    category = "Standard"
else:
    category = "Basic"

# Print customer report
print(f"Customer Report for {customer_name}:")
print(f"- Age Status: {age_status}")
print(f"- Category: {category}")