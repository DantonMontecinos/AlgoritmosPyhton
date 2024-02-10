"""
    Desempeño 62
• Desarrollar un programa con dos funciones.
La primera solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. Llamar desde el bloque del programa principal a ambas funciones.
 
def cuadrado():
    num = int(input("Ingresar numeros: "))
    cuadrado=num**2
    return cuadrado
resultado=cuadrado()
print("El cuadrado es: ",resultado)

def mult():
    num1=int(input("Ingresar primer num: "))
    num2=int(input("Ingresar segundo num: "))
    producto = num1*num2
    return producto
resultado2=mult()
print("El producto es:",resultado2)
Desempeño 63
• Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)programa principal a ambas funciones.

def mayor():
    lista=[]
    for i in range(3):
        num=int(input("Ingresar numeros: "))
        lista.append(num)
    mayor=lista[0]
    for x in range(1,3):
        if lista[x]>mayor:
            mayor=lista[x]
    print(mayor)
mayor()
mayor()

EJEMPLO 52
Identificador de enteros
Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de
los valores hacerlo por teclado. 

def mayor(n1,n2,n3):
    lista=[]
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)
    mayor= lista[0]
    for i in range(1,3):
        if lista[i]>mayor:
            mayor=lista[i]
    print(mayor)
def cargar():
    n1=int(input("Ingresar num: "))
    n2=int(input("Ingresar num: "))
    n3=int(input("Ingresar num: "))

    mayor(n1,n2,n3)
cargar()


EJEMPLO 53
Calculador de perímetro y superficie para un cuadrado
Desarrollar un programa que permita ingresar el lado de un cuadrado.
Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.


def perimetro_super(n1):
    decision = input("Desea perimetro o superficie? p/s: ")
    if decision=="p":
        perimetro= n1*4
        print("El perimetro de:",n1,"es",perimetro)
    else:
        if decision=="s":
            sueperficie= n1**2
            print("La superficie de:",n1,"es",sueperficie)
        else:
            print("No correspondes")

def cargar():
    numero= int(input("Ingresare numero: "))
    perimetro_super(numero)
cargar()

Desempeño 64
• Desarrollar una función que reciba un string como parámetro y nos muestre la cantidad de
vocales. Llamar a la función desde el bloque principal del programa 3 veces con string distintos.

def vocales(palabra):
    contador=0
    for i in range(len(palabra)): 
        if palabra[i]=="a" or palabra[i]=="e" or palabra[i]=="i" or palabra[i]=="o" or palabra[i]=="u":
            contador+=1
    print("Tiene:",contador,"Vocales")

def cargar():
    frase = input("Ingresar palabra: ")
    vocales(frase)
    
cargar()

Desempeño 65
• Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor.
En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer
función definida.


def menor_mayor(n1,n2,n3):
    lista=[]
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)
    print(lista)
    for x in range(2):   
        for i in range(2):
            if lista[i]>lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
    print(lista)

def cargar():
    num1 = int(input("Ingresar numero: "))
    num2 = int(input("Ingresar numero: "))
    num3 = int(input("Ingresar numero: "))
    menor_mayor(num1,num2,num3)
    
cargar()

EJEMPLO 54
Calculador de superficie de cuadrado
Confeccionar una función a la que le enviemos como parámetro el valor
del lado de un cuadrado y nos retorne su superficie.

def superficie(lado):
    super = lado*4
    return super

lado_c= int(input("Ingresar lado: "))

result=superficie(lado_c)
print(result)


Identificador de número mayor
Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
| Programa:



def mayor(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
num1=int(input("Ingresar numero: "))
num2=int(input("Ingresar num: "))

print(mayor(num1,num2))

Contador de caracteres y muestra del mas largo
Confeccionar una función que le enviemos como parámetro un string y
nos retorne la cantidad de caracteres que tiene. En el bloque principal
solicitar la carga de dos nombres por teclado y llamar a la función dos
veces. Imprimir en el bloque principal cual de las dos palabras tiene
más caracteres.


def mas_caracteres(cadena):
    return (len(cadena))
nombre1=input("Ingresar nombre 1: ")
nombre2=input("Ingresar nombre 2: ")

n1=mas_caracteres(nombre1)
n2=mas_caracteres(nombre2)

if n1>n2:
    print("La primera palabra es mayor: ",n1)
else:
    print("la segunda palabra tiene mas caracteres,",n2)

    Desempeño 66
• Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos

def promedio(n1,n2,n3):
    prom = (n1+n2+n3)//3
    return prom

numero1=int(input("Ingresa num"))
numero2=int(input("Ingresa num"))
numero3=int(input("Ingresa num"))

print(promedio(numero1,numero2,numero3))


Desempeño 67
• Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros
el valor de un lado.



def calcula_perimetro(lado):
    perimetro = lado*4
    return perimetro


lado = int(input("Ingresar lado: "))
print(calcula_perimetro(lado))


Desempeño 68
• Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función
recibe como parámetros los valores de dos lados distintos:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cuál de
los dos tiene una mayor superficie.

def retornar_superficie(lado1,lado2):

    resultado=lado1*lado2
    return resultado
lado_primero=int(input("Ingresar primer lado: "))
lado_segundo=int(input("Ingresar segundo lado: "))
lado_tercero=int(input("Ingresar primer lado: "))
lado_cuarto=int(input("Ingresar segundo lado: "))

cuadrado1 = retornar_superficie(lado_primero,lado_segundo)
cuadrado2 = retornar_superficie(lado_tercero,lado_cuarto)


if cuadrado1>cuadrado2:
    print("El cuadrado 1 tiene mayor superficie: ", cuadrado1)
else:
    print("El cuadradado 2 tiene mayor superficie: ",cuadrado2)

Desempeño 69
• Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad
de letras 'a' o 'A'

def min_mayus(palabra):
    contador=0
    for i in range(len(palabra)):
        if palabra[i]=="a":
            contador+=1
    return contador

palabra= input("Ingresar palabra: ")
palabra=palabra.lower()

p=min_mayus(palabra)
print(p)

"""