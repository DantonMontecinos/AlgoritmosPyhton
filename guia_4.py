"""
Guia 4
EJEMPLO 16
1...3...5...7...
Realizar un programa que imprima todos los números impares que hay
entre 1 y 100.

for i in range(1,100,2):
    print(i)

    EJEMPLO 20
Detector de N valores mayores a 1000
Codificar un programa que lea n números enteros y calcule la cantidad
de valores mayores o iguales a 1000 (n se carga por teclado)


mayores=0
cant=int(input("Ingresar la cantidad de num a evaluar: "))

for i in range(cant):
    num=int(input("Ingresar numeros a evaluar: "))
    if num>=1000:
        mayores+=1
print("Mayores a 1.000:",mayores)

Desempeño 26
• Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
a| De cada triángulo la medida de su base, su altura y su superficie.
b| La cantidad de triángulos cuya superficie es mayor a 12 (la superficie se calcula multiplican-
do la base por la altura y a este valor se divide en 2)


cantidad_pares=int(input("Ingresar cantidad pares: "))
contador=0
for i in range(cantidad_pares):
    base = int(input("Ingresa la base: "))
    altura = int(input("Ingresar la altura: "))
    superficie = base*altura
    print("Base:",base,"Altura:",altura,"Superficie:",superficie)
    if superficie>=12:
        contador+=1
print("Triangulos con superficie mayor a 12: ",contador)
Desempeño 27
• Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

suma=0
for i in range(1,11):
    numeros = int(input("Ingresar numeros: "))
    if i>5:
        suma= suma+numeros
print("Suma",suma)

Desempeño 28
| Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)

for i in range(1,51):
    print("5 *",i,":",i*5)

Desempeño 29
• Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de
multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36



numero = int(input("Ingresar numero del 1 al 10: "))
for i in range(1,13):
    print(numero,"*",i,":",numero*i)

    Desempeño 30
• Realizar un programa que lea los lados de n triángulos, e informar:
a| De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b| Cantidad de triángulos de cada tipo.



cantidad_triangulos=int(input("Ingresar cantidad pares: "))
equilateros=0
isosceles=0
escaleno=0

for i in range(cantidad_triangulos):
    primer_lado = int(input("Primer lado: "))
    segundo_lado = int(input("Segundo lado: "))
    tercer_lado = int(input("Tercer lado: "))

    if primer_lado==segundo_lado and primer_lado==tercer_lado:
        equilateros+=1
    else:
        if segundo_lado==tercer_lado or segundo_lado==primer_lado:
            isosceles+=1
        else:
            escaleno+=1
print("Equilatero:",equilateros,"Isosceles:",isosceles,"Escalenos:",escaleno)


Desempeño 31
Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al
comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
1º Cuadrante: x > 0 , y > 0
2º Cuadrante: x < 0 , y > 0
3º Cuadrante: x < 0 , y < 0
4º Cuadrante: x > 0 , y < 0

cantidad=int(input("Ingresar cuantos puntos se analizaran: "))
primer=0
segundo=0
tercer=0
cuarto=0
for i in range(cantidad):
    x=int(input("Ingresar coordenada x: "))
    y=int(input("Ingresar coordenada y: "))

    if x > 0 and y > 0:
        primer+=1
    else:
        if x < 0 and y > 0:
            segundo+=1
        else:
            if x < 0 and y < 0:
                tercer+=1
            else:
                cuarto+=1

print("primer cuadrante:",primer,"Segundo:",segundo,"Tercer:",tercer,"Cuarto:",cuarto)

Desempeño 32
• Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a| La cantidad de valores ingresados negativos.
b| La cantidad de valores ingresados positivos.
c| La cantidad de múltiplos de 15.
d| El valor acumulado de los números ingresados que son pares

negativos=0
positivos=0
multiplos=0
pares=0

for i in range(5):
    numero=int(input("Ingresar: "))
    if numero<0:
        negativos+=1
    else:
        if numero>0 and numero%2 !=0:
            positivos+=1
        else:
            if numero%15 == 0:
                multiplos+=1
                print(numero)
            else:
                if numero%2==0:
                    pares+=1
print("Negativos:",negativos,"Positivos:",positivos,"Multiplos:",multiplos,"Pares:",pares)




Escribir un programa que utilice los siguientes datos:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
y los procese para responder a las siguientes consignas:
a| Obtener el promedio de las edades de cada turno (tres promedios)
b| Imprimir dichos promedios (promedio de cada turno)
c| Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio
de edades mayo

mañana=0
tarde=0
noche=0

for i in range(4):
    edades=int(input("Ingresar edades turno mañana: "))
    mañana=mañana+edades
mañana=mañana//4
print(mañana)
for x in range(4):
    edades=int(input("Ingresar edades turno tarde: "))
    tarde=tarde+edades
tarde=tarde//4
print(tarde)
for i in range(4):
    edades=int(input("Ingresar edades turno noche: "))
    noche=noche+edades
noche=noche//4
print(noche)

if mañana>tarde and mañana>noche:
    print("Mayor romedio edad mañana: ",mañana)
else:
    if tarde>noche:
        print("Mayor romedio edad tarde: ",tarde)
    else:
        print("Mayor romedio edad noche: ",noche)

        Desempeño 34
• Confeccionar un programa que solicite la carga de 10 valores flotantes
(con parte decimal) por teclado. Mostrar al final su suma.
Definir varias líneas de comentarios indicando el nombre del programa,
el programador y la fecha de la última modificación.
Utilizar el caracter # para los comentarios
      
suma=0
for i in range(5):
    num=float(input("Ingresar numeros: "))
    suma=suma+num
print(suma)


condicion="si"
suma=0

while condicion=="si":
    numero=int(input("Ingresar numero: "))
    suma=suma+numero
    condicion=input("Desea sumar otro numero: ")

print(suma)
"""