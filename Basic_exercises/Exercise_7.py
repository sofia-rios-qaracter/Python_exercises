from getters import get_int

print("We are going to count how many multiples of 3 and 5 you give.")
print("For stoping enter the number -1")

readed_number = 0
multiples_of_three = 0
multiples_of_five = 0
multiples_of_both = 0

while (readed_number != -1):
    readed_number = get_int("Give a number: ", "Please type a number")

    if readed_number > 0:
        if readed_number % 3 == 0 and readed_number % 5 == 0:
            multiples_of_both += 1
        elif readed_number % 3 == 0:
            multiples_of_three += 1
        elif readed_number % 5 == 0:
            multiples_of_five += 1
    elif readed_number != -1:
        print("Please type a positive number")


print(f"Total of multiples of three: {multiples_of_three}")
print(f"Total of multiples of five : {multiples_of_five}")
print(f"Total of multiples of both : {multiples_of_both}")