def data_processor(data_list):
    temperatures = []

    for data in data_list:
        if type(data) is int and data >= 0:
            temperatures.append(data)
        elif type(data) is str and data == "offline":
            break

    total_temperatures = len(temperatures)
    mean_temperature = sum(temperatures)/total_temperatures
    greater_than_mean = 0

    for temperature in temperatures:
        if temperature > mean_temperature:
            greater_than_mean += 1


    print("="*20)
    print(f"Total of temperatures:          {total_temperatures}")
    print(f"Mean temperature:               {mean_temperature}")
    print(f"Temperatures greater than mean: {greater_than_mean}")
    print("="*20)

ios_monitoring_data = [22, "ok", 30, -5, 28, "maintenance", 35, "offline", 40]

data_processor(ios_monitoring_data)