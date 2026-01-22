def fitness_aplication(workout_list):
    valid_days = 0
    total_of_exercise_minutes = 0
    intense_workout_days = 0
    average_minutes = 0

    for time_working in workout_list:
        if type(time_working) is str:
            match time_working:
                case "rest":
                    valid_days += 1
                case "error":
                    continue
                case "stop":
                    break
        elif type(time_working) is int or type(time_working) is float:
            if time_working < 0:
                continue
            else:
                #Se podría añadir un if para no sumar el 0 pero sumar 0 no suma nada asi que he decidido dejarlo asi
                total_of_exercise_minutes += time_working 
                valid_days += 1
                if time_working > 60:
                    intense_workout_days += 1
    
    if valid_days > 0:
        average_minutes = total_of_exercise_minutes/valid_days

    return {
        "Total_valid_days": valid_days,
        "Total_exercise_minutes": total_of_exercise_minutes,
        "Number_of_intense_workout_days": intense_workout_days,
        "Average_minutes_per_day": average_minutes
    }

working_list = ["rest", 45, 0, "error", 60, -10, 90, "stop", 30]

print(fitness_aplication(working_list))