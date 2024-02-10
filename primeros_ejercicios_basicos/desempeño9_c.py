"""Confeccionar un programa que permita cargar un número entero positivo de hasta tres ci-
fras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras.
Mostrar un mensaje de error si el número de cifras es mayor
"""
num = int(input("Ingrese un numero: "))

if num>=100 and num<=999:
    print("EL numero tiene tres cifras")
    

else:
    if num>=1000:
        print("Tiene 4 digitos")

    elif num>=10:
        print("Tiene 2 digitos")
    else:
        print("Tiene un digito")

  


