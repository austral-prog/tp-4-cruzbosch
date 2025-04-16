def line():
    A = input("Ingrese el coeficiente A: ")
    B = input("Ingrese el coeficiente B: ")
    X1 = input("Ingrese el coeficiente X1: ")
    X2 = input("Ingrese el coeficiente X2: ")

    print("El coeficiente A de su ecuación de la recta es: " + format(float(A), '.1f'))
    print("El coeficiente B de su ecuación de la recta es: " + format(float(B), '.1f'))
    print("El coeficiente X1 de su ecuación de la recta es: " + format(float(X1), '.1f'))
    print("El coeficiente X2 de su ecuación de la recta es: " + format(float(X2), '.1f'))
    
    A = float(A)
    B = float(B)
    X1 = float(X1)
    X2 = float(X2)
    
    print()
    print("Para la siguiente ecuación:")
    print("\tY = {}X + {}".format(A, B))

    Y1 = A * X1 + B
    Y2 = A * X2 + B

    print()
    print("Dados los siguientes puntos:")
    print("\tP1 ({}, {})".format(X1, Y1))
    print("\tP2 ({}, {})".format(X2, Y2))

    D = ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5
    print()
    print("La distancia entre ellos es: {}".format(D))
