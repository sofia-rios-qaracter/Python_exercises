from getters import get_int

multiplication = 1

for i in range(6):
    given_number = get_int("Give a number: ", "Pleas type a number")
    multiplication *= given_number

print(f"The multiplication of all given numbers is: {multiplication}")