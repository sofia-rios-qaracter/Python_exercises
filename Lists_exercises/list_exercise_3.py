exam_scores = [45, 78, 62, 49, 90, 55, 38]
passing_scores = []

for exam in exam_scores:
    if exam >= 50:
        passing_scores.append(exam)

passing_total = len(passing_scores)
percentage_passed = (passing_total/len(exam_scores))*100

print(f"The exam has been passed by {passing_total} students")
print(f"The percentage of passed exams is {percentage_passed}%")