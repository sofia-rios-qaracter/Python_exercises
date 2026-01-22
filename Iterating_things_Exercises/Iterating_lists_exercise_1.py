def scores_analizer(scores):
    total_valid_scores = 0 # Includes 0 cases
    total_points = 0
    number_of_excellent_scores = 0 # Greater than 9

    for score in scores:
        if score > 11:
            break
        elif score < 0:
            continue
        else:
            total_valid_scores += 1
            total_points += score
            if score > 9:
                number_of_excellent_scores += 1

    return {
        "Total_valid_scores": total_valid_scores,
        "Total_points": total_points,
        "Number_of_excellent_scores": number_of_excellent_scores
    }

scores = [5, 7, -2, 10, 8, 0, 12]

print(scores_analizer(scores))