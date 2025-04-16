def line():
    CoA = float(input("Ingrese el coeficiente A:"))
    CoB = float (input ("Ingrese el coeficiente B:"))
    CoX1 = float (input ("Ingrese el coeficiente X1:"))
    CoX2 = float (input ("Ingrese el coeficiente X2:"))
    Y1 = CoA * CoX1 + CoB
    Y2 = CoA * CoX2 + CoB
    Distancia = ((CoX2 - CoX1)**2 + (Y2 - Y1)**2)**0.5

    print (f"El coeficiente A de su ecuación de la recta es: {CoA}")
    print (f"El coeficiente B de su ecuación de la recta es: {CoB}")
    print (f"El coeficiente X1 de su ecuación de la recta es: {CoX1}")
    print (f"El coeficiente X2 de su ecuación de la recta es: {CoX2}")

    print ("")

    print ("Para la siguiente ecuación:")
    print (f"\tY = {CoA}X + {CoB}")

    print ("")

    print ("Dados los siguientes puntos:")
    print (f"\tP1 ({CoX1}, {Y1})")
    print (f"\tP2 ({CoX2}, {Y2})")

    print ()

    print (f"La distancia entre ellos es: {Distancia}")

line()
