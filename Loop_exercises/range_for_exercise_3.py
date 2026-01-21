divisible_by_four = 0
between_thirty_and_ninety = 0

for i in range(1, 101):
    if i%4 == 0: divisible_by_four += 1
    if i >= 30 and i <= 90: between_thirty_and_ninety += 1

print("\n"+"="*40+"\n")

print(f"Total of divisibles by four: {divisible_by_four}")
print(f"Total of numbers between 30 and 90: {between_thirty_and_ninety}")

print("\n"+"="*40+"\n")