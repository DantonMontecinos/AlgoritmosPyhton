"""
Desempeño 10
• Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha
corresponde a Navidad...
"""
dia = int(input("Ingrese dia: "))
mes = int(input("Ingrese mes: "))
año = int(input("Ingrese año: "))

if mes==12 and dia==24:
    print("Navidad")
else:
    print("No es navidad")