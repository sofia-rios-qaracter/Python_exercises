avg = 0
total = 0

greater_than_average = 0

for i in range(1, 50):
    total += 1
    avg += i

avg /= total

for i in range(1, 50):
    if i > avg: greater_than_average += 1

print("="*20)
print(f" Greater than average: {greater_than_average}")
print("="*20)