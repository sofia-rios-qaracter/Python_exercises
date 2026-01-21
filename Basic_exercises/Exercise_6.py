from getters import get_int

print("We are going to count how many of the given numbers are between 1 and 50 and how many are greater than 50.")
print("For stoping enter the number 0")

readed_number = -1
between_one_and_fifty = 0
greater_than_fifty = 0

while (readed_number != 0):
    readed_number = get_int("Give a number: ", "Please type a number")

    if(readed_number > 0 and readed_number <= 50):
        between_one_and_fifty += 1
    elif(readed_number > 50):
        greater_than_fifty += 1
    elif(readed_number < 0):
        print("Please type just positive numbers")

print(f"Total of numbers between one and fifty: {between_one_and_fifty}")
print(f"Total of numbers greater than fifty: {greater_than_fifty}")