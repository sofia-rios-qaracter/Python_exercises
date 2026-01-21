from getters import get_int

greater_than_fifty = 1

for i in range(8):
    given_number = get_int("Give a number: ", "Pleas type a number")
    if given_number > 50: greater_than_fifty += 1

print(f"You have give {greater_than_fifty} numbers greater than fifty") 