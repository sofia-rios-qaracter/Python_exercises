from getters import get_int

positive = 0
negative = 0

for i in range(7):
    given_number = get_int("Give a number: ", "Pleas type a number")
    
    if given_number > 0: positive +=1
    elif given_number < 0: negative += 1

print(f"You have given {positive} positive numbers")
print(f"You have given {negative} negative numbers")