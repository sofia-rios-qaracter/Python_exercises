from getters import get_int

print("We are going to calculate the sum of the given numbers you are giving us.")
print("For stoping enter the number -1")

readed_number = 0
total_numbers = 0
sum_of_all_numbers = 0

while (readed_number != -1):
    readed_number = get_int("Give a number: ", "Please type a number")

    if(readed_number > 0):
        total_numbers += 1
        sum_of_all_numbers += readed_number
    elif(readed_number != -1):
        print("Please type just positive numbers")

print(f"Total of numbers type it: {total_numbers}")
print(f"The total sum is: {sum_of_all_numbers}")