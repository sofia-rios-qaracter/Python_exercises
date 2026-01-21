import numpy as np

def get_skill(position):
    if position == 0:
        return "Strength"
    elif position == 1:
        return "Speed"
    elif position == 2:
        return "Stamina"
    elif position == 3:
        return "Durability"
    elif position == 4:
        return "Agility"
    else: 
        return "Not a valid option"
    
def get_overall(total_points):
    if total_points == -5:
        return "F"
    elif total_points < -3:
        return "E"
    elif total_points < 0:
        return "D"
    elif total_points == 10:
        return "S+"
    elif total_points >= 8:
        return "S"
    elif total_points > 6:
        return "A"
    elif total_points > 4:
        return "B"
    else:
        return "C" 


def get_grades_athlete(means, standar_deviation, athlete):
    better_than_mean = 0
    extraordinary_better = 0
    extraordinary_bad = 0
    athlete_ranking = {}

    for i in range(0, len(athlete)):
        if athlete[i] >= (means[i] + 2*standar_deviation[i]):
            athlete_ranking[get_skill(i)] = "S"
            extraordinary_better += 1
        elif athlete[i] >= (means[i] + standar_deviation[i]):
            athlete_ranking[get_skill(i)] = "A"
            extraordinary_better += 1
        elif athlete[i] >= means[i]:
            athlete_ranking[get_skill(i)] = "B"
            better_than_mean += 1
        elif athlete[i] < (means[i]- 2*standar_deviation[i]):
            athlete_ranking[get_skill(i)] = "E"
            extraordinary_bad += 1
        elif athlete[i] < (means[i]- standar_deviation[i]):
            athlete_ranking[get_skill(i)] = "D"
        else:
            athlete_ranking[get_skill(i)] = "C" 
    
    total_points = better_than_mean + 2*extraordinary_better - extraordinary_bad

    athlete_ranking["Overall"] = get_overall(total_points)

    return athlete_ranking

# Strength - Speed - Stamina - Durability - Agility
athletes = np.array([
    [85, 78, 90, 88, 80],
    [70, 92, 75, 70, 95],
    [88, 85, 82, 91, 87],
    [60, 65, 70, 60, 68],
    [95, 90, 88, 92, 91],
    [78, 80, 85, 83, 79]
])

means = np.mean(athletes, axis=0)
standard_variation = np.std(athletes, axis = 0)

grades = []

for athlete in athletes:
    athlete_grade = get_grades_athlete(means, standard_variation, athlete) 
    grades.append(athlete_grade)
    print(athlete_grade)

min = np.max(athletes)
max = np.min(athletes)

for athlete in athletes:
    print((athlete-min)/(max-min))
    # athletes_standarice.append((athletes_standarice-min)/(max-min))