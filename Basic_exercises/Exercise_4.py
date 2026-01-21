from getters import get_float, get_int, get_str

USER_ID = get_str("What's your ID?: ", "Please give a correct ID")
AGE = get_int("What's your age?: ", "Please give a number as an answer")
MONTHLY_INCOME = get_float("What's your monthly income?: ", "Give the number as a float please")
NUMBER_FAILED_ATTEMPTS = get_int("How many times have you failed to login?: ", "Please give a number as an answer")

if AGE >= 18:
    if MONTHLY_INCOME >= 2000:
        if NUMBER_FAILED_ATTEMPTS <= 3:
            access_type = "Full"
        else:
            access_type = "Restricted"
    else:
        if NUMBER_FAILED_ATTEMPTS <= 1:
            access_type = "Limited"
        else:
            access_type = "No"
else:
    access_type = "No"

access_type += " Access"

print(f"Your access type is: {access_type}")        
print(f"{USER_ID} - Age: {AGE} Monthly Income of: {MONTHLY_INCOME}€ Failed attempts: {NUMBER_FAILED_ATTEMPTS}")
