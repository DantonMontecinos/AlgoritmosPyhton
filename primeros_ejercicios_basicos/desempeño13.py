"""
Desempeño 13
• Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10,
imprimir en pantalla la leyenda "Alguno de los números es menor a diez".
"""

num1 = int(input("Ingrese primer: "))
num2 = int(input("Ingrese segundo: "))
num3 = int(input("Ingrese tercer: "))

if num1>10 and num2>10 and num3>10:
    print("Todos matyores a 10")
else:
    print("Hay por lo menos uno menor a 10")