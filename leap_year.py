def leap_year():
    año = int(input("Ingrese un año:"))
    if año % 100 == 0 and año % 400 != 0:
        print (f"El año {año} no es bisiesto")
    elif año % 4 != 0:
        print(f"El año {año} no es bisiesto")
    else:
        print(f"El año {año} es bisiesto")
        
leap_year()
