def hours_analizer(list_of_hours):
    total_valid_working_days = 0
    total_hours_worked = 0
    number_of_overtime_days = 0

    for day_hours in list_of_hours:
        if day_hours < 0:
            continue
        elif day_hours > 10:
            break
        elif day_hours != 0:
            total_valid_working_days += 1
            total_hours_worked += day_hours

            if day_hours > 8:
                number_of_overtime_days += 1

    return {"Total_of_valid_working_days": total_valid_working_days, "Total_of_hours_worked": total_hours_worked, "Number_of_overtime_days": number_of_overtime_days}


hour_list = [8, 7, -1, 9, 0, 6, 10]

print(hours_analizer(hour_list))