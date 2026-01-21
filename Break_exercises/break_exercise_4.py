for i in range(1, 41):
    if i%5 == 0:
        if i%8==0:
            break
        # Este else con el continue podrían omitirse
        # Ya que de no entrar al if tampoco se hace nada
        else:
            continue 
    else:
        print(i)