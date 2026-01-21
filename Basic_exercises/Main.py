sales = 150
price = 9.99
customer_price = "Alice"

# Integer (int)
units_sold = 120
customer = 46

# Floating point (float)
price = 19.95
tax_rate = 0.21
average_score = 7.8

# String (str) "H" "" "hello"
product_name = "Laptop"
category = "Electronics"
order_id = "ORD_1023"

# Boolean (bool) -> have/to be
is_active = True
has_discount = False
is_premium_member = True

# Type of a variable -> type()
print(type(price))        # <class 'float'>
print(type(product_name)) # <class 'str'>
print(type(is_active))    # <class 'bool'>

# PEP 8 Style guide
# (OK) Letters (a-z, A-Z), Numbers (not at the beginning), Underscores (_)
# (NO) spaces, special characters, starting with a number
# Use snake_case

# Bad name examples:
x = 120
y = 9.99

# Good name examples:
units_sold = 120
unit_price = 9.99

# Constant
TAX_RATE = 0.21
MAX_USER = 1000
PI = 3.14159

# Example
TAX_RATE = 0.21

price = 100
final_price = price + (price * TAX_RATE)

print(final_price)  # 121.0

#Reassigning variables
sales = 100
sales = sales + 50
print(sales)  # 150

# ------ OPERATORS ------
# Arithmetic Operators: +, -, *, /, %, **, //
a = 10
b = 3

result = a+b   # 13
result = a-b   # 7
result = a*b   # 30
result = a/b   # 10/3 = 3.3333...   -> When you need precision
result = a//b  # 10/3 = 3           -> When you need whole number
result = a%b   # 10%3 = 1
result = a**b  # 1000

# 2 4 6 8 10 -> Even numbers
# 1 3 5 7 9  -> Odd numbers

result = 10%2  # 0 (even)
result = 9%2   # 1 (odd)

# Comparison Operators: ==, !=, >, <, >=, <= Return a boolean
is_equal = a==b    # False
not_equal = a!=b  # True
greater = a>b     # True
greater_than_or_equal = a>=b  # True
less_than_or_equal = a<=b  # False 

# Example
result = 10>10  # False
result = 10>=10 # True

result = (1== 1) and (2==2)  # True
result = (1==1) or (2==3)    # True
result = not(1==1)           # False

## Asignment Operators: =, +=, -=, *=, /=, %=, //=, **=
x = 5
x += 2
x -= 3
x *= 4
x /= 2
x %= 3
x //= 2
x **= 3

total_sales = 0

total_sales += 120
total_sales += 300

# Type Conversion -> Casting
# int(), float(), str(), bool()

units = "150"
units = int(units)  # Convert string to integer
value = bool(0)    # false
value = bool(1)    # true
value = bool("")   # false
value = bool("Hello")  # true
value = bool([])    # false
value = bool({"hola": "adios"})  # false

print(value)

# age = input("How old are you? ")  # Input returns a string
# print(type(age))  # <class 'str'>

# print()
object_estrange = {"key": "value"}
print(str(object_estrange))  # Convert to string before printing

customer = "Alice"
sales = 960.2

print(f"Customer {customer}: sales {sales}€")

"""
Hello, I'm Alice.
Total sales: 960.2€
"""

# If - Else Statement
"""
Sintax (cuidado con las tabulaciones por que son importantes): 
if condition:
    code_if_condition_true
else:
    code_if_condition_false
"""

age = 27

# age = int(input("How old are you? "))

if age >= 18: # Vale cualquier tipo de condicion de las vistas antes !=, ==, >, <, >=, <= y se pueden concatenar con and, or, not
    print("You are an adult.")
else:
    print("You are a minor.")

print("Out of if-else")

"""
if condition_1:
    code_1
elif condition_2:
    code_2
elif condition_3:
    code_3
else: # No es obligatorio poner un else
    code_default
"""

monthly_spending = float(input("How many money do you spent?: "))

if monthly_spending >= 1000:
    category = "Premium"
elif monthly_spending >= 500:
    category = "Standard"
else:
    category = "Basic"

print(f"Your category is: {category}")

sales = 1200
is_active = True

if sales > 1000 and is_active:
    print("Nice!")

role = "admin"
is_manager = False

if role == "admin" or is_manager:
    print("Nice!")

is_blocked = False

if not is_blocked:
    print("You can use it")

age = 25
has_id = True


if has_id:
    if age >= 18:
        print("Access granted")
    else:
        print("Access denied")
else: 
    print("Access denied")
