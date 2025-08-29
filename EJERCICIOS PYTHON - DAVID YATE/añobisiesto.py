año = float(input("Ingrese el año"))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print (f"El {año} es bisiesto")
else:
    print (f"El {año} no es bisiesto")