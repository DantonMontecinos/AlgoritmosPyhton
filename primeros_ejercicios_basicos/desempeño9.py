""""
Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.
"""

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
num3 = int(input("Ingrese tercer numero: "))

if num1>num2 and num3:
    print("El numero: "+str(num1)+" es el mayor")
else:
    if num2>num1 and num2>num3:
        print("El numero: "+str(num2)+" es el mayor")
    else:
        print("El numero: "+str(num3)+" es el mayor")

