#Realizá un programa que solicite la carga por teclado de dos números,
#si el primero es ma-yor
#al segundo mostrá por pantalla su suma y diferencia, en caso contrario informá el producto
#y la división del primero respecto al segundo

print("_____Ingrese dos numeros_____")
num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))


if num1>num2:

    suma=num1+num2
    resta=num1-num2
    print("La suma de: "+str(num1)+" y "+str(num2)+" es: "+str(suma))
    print("La resta de: "+str(num1)+" y "+str(num2)+" es: "+str(resta))
else:
    
    
    multi = num2*num1
    division=num2/num1
    print("La division de: "+str(num2)+" y "+str(num1)+" es: "+str(division))
    print("La multi de: "+str(num2)+" y "+str(num1)+" es: "+str(multi))
