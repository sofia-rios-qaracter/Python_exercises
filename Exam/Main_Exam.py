"""
PYTHON DATA ANALYSIS EXAM (2 hours)
Scenario: E-commerce order records audit

Expected logical structure per record:
order_id ; email ; amount ; status
"""

# =========================
# Objective 1 — Raw data setup (8 points)
# =========================
# Create a list containing at least 14 raw order records (strings).
# Include both correct and incorrect records.
# Examples of issues to include:
# - extra spaces
# - mixed upper/lower case
# - currency symbols or text
# - comma decimals
# - invalid status
# - missing fields
# - negative amounts

# TODO:
# 1) Store the raw records in a list
# 2) Print how many raw records exist

VALID_STATUSES = ["delivered", "pending", "canceled", "completed"]
HIGH_VALUE_THRESHOLD = 100.0
MIN_VALID_AMOUNT = 0
CURRENCY_SYMBOLS = ["€", "$", "eur", "usd"]

email = "example_email@gmail.com"

raw_dataset = [
    f"ord_1; {email}       ; 3,6usd; PENDING",
    f"ord_2; example_email@hotmail.com; 3.5eur; completed",
    f"ord_3; {email}; 3€; delivered     ",
    f"ord_4; {email}; -4; pending",
    f"ord_5; {email}; 101.5; delivered",
    f"ord_6; {email}; 3.7; delivered",
    f"7; {email.upper()}; 3USD; none;",
    f"ord_8€; {email}; 3; completed",
    f"ord_9; {email}; 3, none",
    f"ord_10; {email}; 3; delivered",
    f"ord_11; bademail.com; 3.3; completed",
    f"ord_12; {email}; 0 ; pending",
    f"13; {email}; 3; completed",
    f"ord_14; {email.upper()}"
]

print("="*30)
print("Exercise 1")
print("Raw data:")
print(raw_dataset)
print("="*30)

# =========================
# Objective 2 — Cleaning records (10 points)
# =========================
# Define a function that receives ONE raw record and returns a cleaned version.
# Cleaning rules:
# - remove leading/trailing spaces
# - convert text to lowercase
# - remove currency symbols/text
# - replace comma decimals with dot decimals
# - remove spaces around separators

# TODO:
# 1) Define the cleaning function
# 2) Create a new list with all cleaned records
# 3) Print the first three cleaned records

def string_removal_spaces_and_currency_symbols(text):
    good_text = text.strip()

    for currency_symbol in CURRENCY_SYMBOLS:
        splited_text = good_text.split(currency_symbol)
        
        good_text = ""

        for text in splited_text:
            good_text += text.strip()
    
    return good_text

def replace_coma_for_dot(text):
    good_text = ""
    splited_text = text.strip().split(",")
    total_of_comas = len(splited_text)-1 # Se le ha restado uno para que sea de verdad la cantidad de comas en el texto

    if total_of_comas == 0:
        if splited_text[0].count(".") == 0:
            good_text = splited_text[0]+".0"
        else:
            good_text = splited_text[0]
    elif total_of_comas == 1:
        good_text = splited_text[0].strip()+"."+splited_text[1].strip()

    # Si hay mas de 1 coma entonces esta mal el dato y devolvemos ""

    return good_text

def good_status(text):
    good_text = text.lower().strip()
    
    if good_text in VALID_STATUSES:
        return good_text
    else:
        return ""
    
def data_line_cleaner(data_line):
    good_data = ""
    data = data_line.lower().split(";")

    if len(data) == 4:
        good_data += string_removal_spaces_and_currency_symbols(data[0])
        good_data += ";"
        good_data += string_removal_spaces_and_currency_symbols(data[1])
        good_data += ";"
        good_data += string_removal_spaces_and_currency_symbols(replace_coma_for_dot(data[2]))
        good_data += ";"
        good_data += good_status(data[3])
    else:
        good_data += string_removal_spaces_and_currency_symbols(data_line.lower())

    
    return good_data

def data_cleaner(raw_data):
    data_cleaned = []
    for data in raw_data:
        data_cleaned.append(data_line_cleaner(data))
    return data_cleaned

data_cleaned = data_cleaner(raw_dataset)

print("Exercise 2")
print(data_line_cleaner(data_cleaned[0]))
print(data_line_cleaner(data_cleaned[1]))
print(data_line_cleaner(data_cleaned[2]))
print("="*30)
        

# =========================
# Objective 3 — Validation and separation (14 points)
# =========================
# Separate valid and invalid records.
# A record is valid if:
# - it contains exactly 4 fields
# - the order id starts with "ord_"
# - the email contains "@"
# - the status is one of the valid statuses
# - the amount is a number >= MIN_VALID_AMOUNT

# TODO:
# 1) Create empty lists for valid data (ids, emails, amounts, statuses)
# 2) Create a list for invalid records
# 3) Loop through cleaned records and validate them
# 4) Store valid data in separate lists
# 5) Store invalid records separately
# 6) Print how many valid and invalid records exist

def just_valid_data(data):
    valid_data = []
    invalid_data = []

    for data_row in data:
        data_row_splited = data_row.split(";")
        
        if len(data_row_splited) != 4:
            invalid_data.append(data_row)
        else:
            id = data_row_splited[0]
            email = data_row_splited[1]
            amount = float(data_row_splited[2])
            status = data_row_splited[3]

            if id == "" or email == "" or amount == "" or status == "":
                invalid_data.append(data_row)
            elif amount < MIN_VALID_AMOUNT:
                invalid_data.append(data_row)
            elif email.count("@") != 1:
                invalid_data.append(data_row)
            elif not id.startswith("ord_"):
                invalid_data.append(data_row)
            else:
                valid_data.append([id, email, amount, status])

    return (valid_data, invalid_data)

(valid_data, invalid_data) = just_valid_data(data_cleaned)

print("Exercise 3")
print(f"Valid data: {len(valid_data)}")
print(f"Invalid data: {len(invalid_data)}")
print("="*30)

# =========================
# Objective 4 — Filter completed orders (10 points)
# =========================
# From the valid data, extract only the amounts of completed orders.

# TODO:
# 1) Create a list with amounts of completed orders
# 2) Print how many completed orders exist

def status_orders(orders, status):
    completed_orders = []
    for order in orders:
        if order[3] == status:
            completed_orders.append(order)
    
    return completed_orders

def just_completed_orders(orders):
    return status_orders(orders, "completed")

completed_orders = just_completed_orders(valid_data)
print("Exercise 4")
print(f"Completed orders: {len(completed_orders)}")
print("="*30)

# =========================
# Objective 5 — Total and average calculation (12 points)
# =========================
# Create reusable functions to calculate:
# - total
# - average
# If a list is empty, return 0.

# TODO:
# 1) Define a function to calculate a total
# 2) Define a function to calculate an average
# 3) Calculate and print total and average of completed orders

def total(completed_orders):
    total = 0
    for order in completed_orders:
        total += order[2]

    return total

def average(completed_orders):
    total_price = total(completed_orders)
    good_orders = len(completed_orders)

    if good_orders != 0:
        return total_price / good_orders
    else:
        return 0

print("Exercise 5")
print(f"Total:   {total(completed_orders)}")
print(f"Average: {average(completed_orders)}")
print("="*30)

# =========================
# Objective 6 — Highest completed order (10 points)
# =========================
# Find the completed order with the highest amount.
# Show:
# - order id
# - email
# - amount
# If there are no completed orders, show a message.

# TODO:
# 1) Check if completed orders exist
# 2) Find the highest amount manually
# 3) Retrieve related order id and email
# 4) Print the result
def get_highest_completed_order(completed_orders):
    if len(completed_orders) == 0: return None

    highest_order = completed_orders[0]

    for order in completed_orders:
        if order[2] > highest_order[2]:
            highest_order = order

    return highest_order

highest_order = get_highest_completed_order(completed_orders)

print("Exercise 6")
print(f"Highest order: {highest_order}")
print("="*30)

# =========================
# Objective 7 — Email domain analysis (8 points)
# =========================
# Count how many valid emails are Gmail and how many are not.

# TODO:
# 1) Count gmail addresses
# 2) Count other addresses
# 3) Print both results

def count_gmail(valid_order):
    gmail_count = 0

    for order in valid_order:
        if len(order[1].split("gmail")) == 2:
            gmail_count += 1
    
    return gmail_count
    
total_gmail = count_gmail(valid_data)

print("Exercise 7")
print(f"Number of Gmail mails: {total_gmail}")
print("="*30)

# =========================
# Objective 8 — Suspicious orders (12 points)
# =========================
# Mark orders as suspicious if:
# - amount >= HIGH_VALUE_THRESHOLD and status is not completed
# - status is pending and amount is 0
#
# Store warning messages as strings.

# TODO:
# 1) Create a list for warning messages
# 2) Loop through valid records and apply the rules
# 3) Print how many suspicious orders were found

def suspicious_orders(valid_orders):
    sus_order = []

    for order in valid_orders:
        amount = order[2]
        status = order[3]

        if amount >= HIGH_VALUE_THRESHOLD and status != "completed":
            sus_order.append(order)
        elif amount == 0 and status == "pending":
            sus_order.append(order)


    return sus_order

sus_orders = suspicious_orders(valid_data)
total_of_sus_orders = len(sus_orders)

print("Exercise 8")
print(f"Suspicious orders found: {total_of_sus_orders}")
print("="*30)

# =========================
# Objective 9 — Final report (10 points)
# =========================
# Create a multi-line text report containing:
# - total raw records
# - valid records
# - invalid records
# - completed total and average
# - highest completed order (or message)
# - email domain counts
# - suspicious order count

# TODO:
# 1) Build the report as a string
# 2) Print the report

def print_valid(valid_data):
    print("-"*20)
    for data in valid_data:
        id = data[0]
        email = data[1]
        amount = data[2]
        status = data[3]

        print(f"Id: {id}")
        print(f"email: {email}")
        print(f"Amount: {amount}")
        print(f"email: {status}")
        print("-"*20)

def print_invalid(invalid_data):
    for data in invalid_data:
        print(data)

print("Exercise 9")

print(f"Total raw records: {len(raw_dataset)}")
print(f"Valid records: ")
print_valid(valid_data)
print(f"Invalid records: ")
print("-"*20)
print_invalid(invalid_data)
print("-"*20)
print(f"Completed total:   {total(completed_orders)}")
print(f"Completed average: {average(completed_orders)}")
print(f"Gmail accounts: {total_gmail}")
print(f"Suspicious order count: {total_of_sus_orders}")

print("="*30)

# =========================
# Objective 10 — User query by status (6 points)
# =========================
# Ask the user for a status to analyze.
# Validate the input.
# If valid, calculate and print the total amount for that status.

# TODO:
# 1) Ask the user for a status
# 2) Validate it
# 3) Calculate and print the total amount

print("Exercise 10")
given_status = input("Searching status: ")

if given_status in VALID_STATUSES:
    list_status = status_orders(valid_data, given_status)
    total_for_status = total(list_status)
    print(f"Total for {given_status}: {total_for_status}")
else:
    print("You have give a not valid status")
print("="*30)