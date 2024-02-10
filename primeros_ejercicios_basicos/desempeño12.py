"""
Desempeño 12
• Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, impri-
mir en pantalla la leyenda "Todos los números son menores a diez"
"""
num1 = int(input("Ingrese primer: "))
num2 = int(input("Ingrese segundo: "))
num3 = int(input("Ingrese tercer: "))

if num1<=10 and num2<=10 and num3<=10:
    print("Todos menores a diez")
else:
    print("Hay por lo mnenos uno mayor a 10")