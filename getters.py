def get_str(message, error_message):
    return get_generico(message, error_message, str)

def get_int(message, error_message):
    return get_generico(message, error_message, int)

def get_float(message, error_message):
    return get_generico(message, error_message, float)

def get_generico(message, error_message, function):
    repeat = True

    while(repeat):
        try:
            repeat = False
            user_input = function(input(message))
        except ValueError:
            print(error_message)
            repeat = True
    return user_input

def summary(table_name, data):
    print("-"*5+f" {table_name} "+"-*5")
    for name, message in data.item():
        print(f"{name}:\t{message}")
    print("-"*(len(table_name)+12))
    