"""
Desempeño 11
• Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con
el segundo y a este resultado se lo multiplica por el tercero
"""
num1 = int(input("Ingrese primer: "))
num2 = int(input("Ingrese segundo: "))
num3 = int(input("Ingrese tercer: "))

if num1==num2 and num2==num3 and num1==num3:
    suma=num1+num2
    mult=suma*num3
    print("Suma: "+str(suma)+" Mult: "+str(mult))
else:
    print("No son iguales")