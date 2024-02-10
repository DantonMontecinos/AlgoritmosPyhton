import random
"""
i=0
while i<100:
    i+=1
    print(i)

    Desempeño 17
| Probemos algunas modificaciones de este programa y veamos que cambios se deberían hacer
para los siguientes enunciados:
a| Imprimir los números del 1 al 500.
b| Imprimir los números del 50 al 100.
c| Imprimir los números del -50 al 0.
d| Imprimir los números del 2 al 100 pero de 2 en 2 (2,4,6,8 ....100)


i=0
while i <=100:
    print("num: ",i)
    i+=1

i=50
while i<=100:
    print("Num: ",i)
    i+=1

i=-50
while i<=0:
    print(i)
    i+=1

i=0

while i<=100:
    i+=2
    print("Num: ",i)
EJEMPLO 12
Enseñandole a contar hasta el número solicitado
Realizá un programa que solicite la carga de un número positivo y nos
muestre desde 1 hasta el valor ingresado de uno en uno de uno en uno.
| Por ejemplo: Si ingresamos 30 se debe mostrar en pantalla los núme-
ros del 1 al 30

i=0
maximo=int(input("Ingresar hasta donde imprimir numeros: "))

while i<maximo:
    i+=1
    print(i)

    EJEMPLO 13
Enseñandole a sumar a nuestro programa
Realizá un programa que permita la carga de 10 valores por teclado y
nos muestre posteriormente la suma de los valores ingresados y tam-
bién su promedio.

i=1
suma=0
while i<=10:
    num=int(input("Ingresar 10 numeros: "))
    suma=suma+num
    i+=1

print(suma)

EJEMPLO 14
Contador de piezas aptas para stock
Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de
piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo
que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30
son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en
el lote.


i=0
contador=0
num=int(input("Ingresar cantidad de piezas: "))
while i<num:
    i+=1
    longitud=float(input("Ingresar longitud: "))
    if longitud>=1.20 and longitud<=1.30:
        contador+=1

print("Cantidad de piezas aptas: ",contador)

Desempeño 18
| Escribir un programa que solicite ingresar 10 notas de alumnos
 y nos informe cuántos tienen
notas mayores o iguales a 7 y cuántos menores

i=0
contador=0

while i<=5:
 
    num=int(input("notas: "))
    if num>=7:
        contador+=1
    i+=1
print("Notas mayores a 7: ",contador)

Desempeño 19
| Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de
las personas.

i=0
contador=0
cantidad=int(input("Ingresar cantidad: "))
while i<cantidad:
    num=float(input("Alturas: "))
    contador = contador+num
    i+=1
promedio = contador/cantidad
print("Promedio: ",promedio)

Desempeño 20
| En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un
programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran en-
tre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe
que gasta la empresa en sueldos al personal

i=0
contador=0
suma=0
num=int(input("Ingresar cantidad de empleados: "))

while i<num:
    sueldos=int(input("Ingresar sueldos: "))
    suma=suma+sueldos
    if sueldos >=100 and sueldos <=300:
        contador+=1
    i+=1
print("Sueldos entre $100 y $300:",contador)
print("Ingresar total sueldos:",suma)


Desempeño 21
| Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc.
(No se ingresan valores por teclado)


i=0
contador=0
while i < 25: 
    print(i*11)
    i+=1
Desempeño 22
| Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.

i=0

while i<500:
    i+=8
    print(i)

    Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un
mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lis-
ta 2 mayor", "Listas iguales")
Tené en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo

i=0
lista=0
lista2=0
while i<5:
    num1=int(input("Ingresar numeros lista 1: "))
    lista=lista+num1
    i+=1
x=0
while x<5:
    num2=int(input("Ingresar numeros lsita 2: "))
    lista2=lista2+num2
    x+=1

if lista==lista2:
    print("Listas iguales")
else:
    if lista>lista2:
            print("Lista 1 mayor: ",lista)
    else:
        print("Lista 2 mayor: ",lista2)
print(lista)
print(lista2)

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



Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados
en forma alfabética.



name1=input("Ingresar primer nombre: ")
name2=input("Ingresar segundo nombre: ")
print(name1,name2)
if name1>name2:
    print(name1,name2)
else:
    print(name2,name1)

EJEMPLO 25
Mostrador de iniciales y su cantidad de caracteres
Realizar la carga del nombre de una persona y luego mostrar el primer
carácter del nombre y la cantidad de letras que lo componen.
 
nombre = input("Ingresar nombre")

print("inicial:",nombre[0])
print("Cantidad de caracteres: ",len(nombre))

Cargador de nombres e identificador de vocales
Solicitar la carga del nombre de una persona en minúsculas. Mostrar
un mensaje si comienza con vocal dicho nombre.

name = input("Ingresar nombre: ")

if name[0]=="a" or name[0]=="e" or name[0]=="i" or name[0]=="o" or name[0]=="u":
    print("Empieza con vocal: ",name[0])
else:
    print("No empieza con vocal: ",name[0])

    EJEMPLO 27
Validador de direcciones de correo
Ingresar un mail por teclado. Verificar si el string ingresado contiene
solo un carácter "@".


email=input("Ingresar email: ")
contador=0
for i in range(len(email)):
    if email[i]=="@":
        contador+=1
if contador>=1:
    print("Tiene un arroba")
else:
    print("No tiene arroba")

Desempeño 36
• Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron.
Tené en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""


frase=input("Ingresar: ")
contador=0
for i in range(len(frase)):
    if frase[i]==" ":
        contador+=1
print(frase,"Tiene: ",contador,"espacios en blanco")

Desempeño 37
• Ingresar una oración que puede tener letras tanto en mayúsculas como minúsculas.
Contar la cantidad de vocales. Crear un segundo string con toda la
oración en minúsculas para
que sea más fácil disponer la condición que verifica que es una vocal.


frase=input("Ingresar oracion: ")
frase = frase.lower()
contador=0

for i in range(len(frase)):
    if frase[i]=="a" or frase[i]=="e" or frase[i]=="i" or frase[i]=="o" or frase[i]=="u":
        contador+=1
print("La frase tiene:",contador," vocales")

Desempeño 38
• Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres.
Controlá que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en el caso
contrario mostrar un mensaje de error


password = input("Ingresar password entre 10 y 20 digitpos: ")

if len(password)>=10 and len(password)<=15:
    print("Password valido",password,"carcateres: ",len(password))
else:
    print("Password invalido:",len(password),"caracteres")

EJEMPLO 29
Lista de elementos a sumar
Definir una lista que almacene 5 enteros. Sumar todos sus elementos y
mostrar dicha suma.



lista=[5,5,5,5,100]
suma=0
for i in range(len(lista)):
    suma = suma+lista[i]
print(suma)

Desempeño 39
• Definir por asignación una lista con 8 elementos enteros. Contar cuántos de dichos valores
almacenan un valor superior a 100.


lista=[]
for i in range(5):
    num = int(input("Ingresar numeros: "))
    lista.append(num)
mayores=0
for x in range(len(lista)):
    if lista[x]>100:
        mayores+=1
print(lista)
print("Valores mayores a 100:",mayores)


Desempeño 40
• Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con
valores iguales o superiores a 7.

lista=[]
for i in range(5):
    num = int(input("Ingresar numeros: "))
    lista.append(num)
mayores=0
for x in range(len(lista)):
    if lista[x]>=7:
        mayores+=1
print(lista)
print("Valores mayores a 7:",mayores)

Desempeño 41
• Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuántos
de esos nombres tienen 5 o más caracteres

lista=[]
for i in range(5):
    names = input("Ingresar nombres: ")
    lista.append(names)
mayores=0
for x in range(len(lista)):
    if len(lista[x])>=5:
        mayores+=1
print(lista)
print("Nomrbes con mas de 5 caracteres:",mayores)

EJEMPLO 33
Creando una lista con el usuario
Realizar la carga de valores enteros por teclado, almacenarlos en una
lista. Finalizar la carga de enteros al ingresar el cero. Mostrar final-
mente el tamaño de la lista.


lista=[]
i=0
condicion=False
while not condicion:
    numero=int(input("Ingresar numeros: "))
    lista.append(numero)
    for i in range(len(lista)):
        if lista[i]==0:
            lista.pop()
            print(lista)
            condicion=True
            
      

lista=[]
numero=int(input("Ingresar cero para finalizar: "))

while numero!=0:
    numero=int(input("Ingresar numeros: "))
    lista.append(numero)
print(lista)

Desempeño 42
• Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

   
lista=[]
i=0
while i < 5:
    sueldos=float(input("Ingresar sueldos: "))
    lista.append(sueldos)
    i+=1
print(lista)
promedio=0
for x in range(len(lista)):
    promedio = promedio+lista[x]
promedio = promedio//5
print(promedio)

Desempeño 43
• Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) Obtener el promedio de la alturas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
   
alturas=[]

for i in range(5):
    altu=float(input("Ingresar alturas: "))
    alturas.append(altu)
promedio=0    
for y in range(len(alturas)):
    promedio = promedio+alturas[y]
promedio = promedio//5

altas=0
bajas=0
for x in range(len(alturas)):
    if alturas[x]>promedio:
        altas+=1
    else:
        bajas+=1
print(alturas)
print("Promedio altura: ",promedio)
print("MAyores promedio:",altas,"Menores al promedio:",bajas)

Desempeño 44
• Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde)
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.


lista1=[]
lista2=[]

for i in range(4):
    sueld = int(input("Ingresar sueldos: "))
    lista1.append(sueld)
    if i==3:
        for x in range(4):
            sueld = int(input("Ingresar sueldos: "))
            lista2.append(sueld)
print(lista1)
print(lista2)

EJEMPLO 34
Creando una lista con el usuario
Crear y cargar una lista con 5 enteros.
Implementar un algoritmo que identifique el mayor valor de la lista.


lista=[]

for i in range(5):
    num =int(input("Ingresar nums: "))
    lista.append(num)
mayor=lista[0]
for x in range(len(lista)):
    if lista[x]>mayor:
        mayor=lista[x]
print("El mayor es: ", mayor)

Desempeño 45
• Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre
de persona menor en orden alfabético.
 
lista=[]

for i in range(5):
    names=input("Ingresar nombres: ")
    lista.append(names)
print(lista)
menor=lista[0]
for x in range(len(lista)):
    if lista[x]<menor:
        menor=lista[x]
print("El menor en orden alfabetico es: ",menor)

Desempeño 46
• Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)


lista=[]

for i in range(5):
    num=int(input("Ingresar numeros: "))
    lista.append(num)
mayor=lista[0] 
print(lista)


for x in range(len(lista)):
    if lista[x]>mayor:
        mayor=lista[x]
repetidos=0
for y in range(len(lista)):
    if mayor==lista[y]:
        repetidos+=1

print("EL mayor de la lista es:",mayor,".Se repite:",repetidos)


EJEMPLO 37
Ordenar una lista de sueldos
Se debe crear y cargar una lista donde almacenar 5 sueldos.
Desplazar el valor mayor de la lista a la última posición.
La primera aproximación para llegar en el próximo problema al ordenamiento completo de una lista tiene por objetivo analizar los intercambios
de elementos dentro de la lista y dejar el mayor en la última posición.
| El algoritmo consiste en comparar si la primera componente es mayor
a la segunda, en caso que la condición sea verdadera, intercambiamos
los contenidos de las componentes.
Vamos a suponer que se ingresan los siguientes valores por teclado:

1200
750
820
550
490


lista=[1200,750,820,550,490]
print(lista)

for x in range(4):
    for i in range(4-x):
        if lista[i]>lista[i+1]:
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux
print(lista)

Desempeño 50
• Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla.
almacenan un valor superior a 100.


lista=["Uruguay","Argentina","Peru","Bolivia","Chile"]
print(lista)
for i in range(4):
    for x in range(4-i):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
print(lista)

Desempeño 51
• Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar una lista con todos los sueldos de dichos empleados. Imprimir la lista de sueldos ordenados de menor a mayor.


cantidad=int(input("Ingresar cantidad: "))
sueldos=[]
for i in range(cantidad):
    sueld = int(input("Ingresar sueldos: "))
    sueldos.append(sueld)
print(sueldos)
for x in range(1,len(sueldos)):
    for i in range(cantidad-x):
        if sueldos[i]>sueldos[i+1]:
            aux=sueldos[i]
            sueldos[i]=sueldos[i+1]
            sueldos[i+1]=aux
print(sueldos)

Desempeño 52
• Cargar una lista con 5 elementos enteros.
Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.

numeros=[]
for i in range(5):
    enteros = int(input("Ingresar sueldos: "))
    numeros.append(enteros)
print(numeros)
for x in range(4):
    for i in range(4-x):
        if numeros[i]>numeros[i+1]:
            aux=numeros[i]
            numeros[i]=numeros[i+1]
            numeros[i+1]=aux

print(numeros)
for y in range(4):
    for x in range(4):
        if numeros[x]<numeros[x+1]:
            aux=numeros[x]
            numeros[x]=numeros[x+1]
            numeros[x+1]=aux
print(numeros)



alumnos=[]
notas=[]

for k in range(5):
    names=input("Ingresar nombres: ")
    alumnos.append(names)
    n=int(input("Ingresar notas: "))
    notas.append(n)
print(alumnos)
print(notas)
for x in range(4):
    for i in range(4):
        if notas[i]>notas[i+1]:
            aux=notas[i]
            notas[i]=notas[i+1]
            notas[i+1]=aux

            aux2=alumnos[i]
            alumnos[i]=alumnos[i+1]
            alumnos[i+1]=aux2
for i in range(len(alumnos)):
    print(alumnos[i],notas[i])

    Desempeño 53
• Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes
del mismo. Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la
cantidad de habitantes (de mayor a menor) e imprimir nuevamente.


paises=[]
habitantes=[]

for y in range(5):
    names=input("Ingresar paises: ")
    paises.append(names)
    cantidad=int(input("Ingresar habitantes: "))
    habitantes.append(cantidad)

print(paises)
print(habitantes)

for x in range(4):
    for i in range(4):
        if paises[i]>paises[i+1]:
            aux=paises[i]
            paises[i]=paises[i+1]
            paises[i+1]=aux

            aux2=habitantes[i]
            habitantes[i]=habitantes[i+1]
            habitantes[i+1]=aux2

for t in range(5):
    print(paises[t],habitantes[t])

for x in range(4):
    for i in range(4):
        if habitantes[i]>habitantes[i+1]:
            aux=habitantes[i]
            habitantes[i]=habitantes[i+1]
            habitantes[i+1]=aux

            aux2=paises[i]
            paises[i]=paises[i+1]
            paises[i+1]=aux2
for u in range(5):
    print(paises[u],habitantes[u])

    EJEMPLO 40
Creando una lista con componentes lista
Crear una lista por asignación. La lista tiene que tener cuatro elementos y cada elemento debe ser una lista de 3 enteros.
Imprimir sus elementos accediendo de diferentes modos.


lista=[]

for i in range(4):
    lista.append([])
    for x in range(3):
        num =int(input("Ingresar numeros: "))
        lista[i].append(num)
print(lista)

EJEMPLO 41
Sumando listas con componentes de tipo lista
Crear una lista por asignación. La lista tiene que tener 2 elementos y
cada elemento debe ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista principal.


lista=[]
for x in range(2):
    lista.append([])
    for i in range(5):
        num=int(input("Ingresar numeros: "))
        lista[x].append(num)
print(lista)
suma=0
for i in range(len(lista)):
    for x in range(5):
        suma=suma+lista[i][x]
print(suma)


Ejemplo
Crear una lista por asignación. La lista tiene que tener 5 elementos.
Cada elemento debe ser una lista, la primera lista tiene que tener un
elemento, la segunda dos elementos, la tercera tres elementos y así sucesivamente. Sumar todos los valores de las listas.

lista=[]
for i in range(5):
    lista.append([])
    for x in range(i+1):
        lista[i].append(x)
suma=0
for x in range(5):
    for i in range(len(lista[x])):
        suma=suma+lista[x][i]

print(lista)
print(suma)

Desempeño 54
• Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista". Volver a imprimir la lista.

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
print(lista)

for i in range(len(lista)):
    for x in range(len(lista[i])):
        if lista[i][x]>=50:
            lista[i][x]=0
print(lista)

Desempeño 55
• Se tiene la siguiente lista:
lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores
a 10 contenidos en el primer elemento de la variable "lista". Volver a imprimir la lista.

lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

for i in range(len(lista[0])):
    if lista[0][i] >=10:
        lista[0][i]=0
print(lista)    


Desempeño 56
• Crear una lista por asignación con la cantidad de elementos de tipo lista que usted desee.
Luego imprimir el último elemento de la lista principal.


cantidad=int(input("Ingresar cantidad listas: "))
lista=[]
for i in range(cantidad):
    lista.append([])
    cantidad=int(input("Cuantos elementos: "))
    for x in range(cantidad):
        elementos= int(input("Ingresar elementos: "))
        lista[i].append(elementos)
print(lista[0][0])
print(lista)

EJEMPLO 44

a| Realizar la carga de los nombres de empleados y los tres sueldos
por cada empleado.
b| Generar una lista que contenga el ingreso acumulado en sueldos
en los últimos 3 meses para cada empleado.
c| Mostrar por pantalla el total pagado en sueldos a cada empleado
en los últimos 3 meses
d| Obtener el nombre del empleado que tuvo el mayor ingreso
acumulado

empelados=[]
sueldos=[]
total=[]
for y in range(3):
    names=input("Ingresar nombre empleado: ")
    empelados.append(names)
    s1=int(input("Ingresar sueldos: "))
    s2=int(input("Ingresar sueldos: "))
    s3=int(input("Ingresar sueldo: "))
    sueldos.append([s1,s2,s3])
suma=0

for x in range(len(sueldos)):
    suma=sueldos[x][0]+sueldos[x][1]+sueldos[x][2]
    total.append(suma)
print(total)

for i in range(3):
    print(empelados[i],total[i])

    
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

EJEMPLO 57
Funciones que retornen la suma, el mayor y el menor
Definir por asignación una lista de enteros en el bloque principal del
programa. Elaborar tres funciones, la primera recibe la lista y retorna
la suma de todos sus elementos, la segunda recibe la lista


def suma(lista):
    suma=0
    for i in range(len(lista)):
        suma=suma+lista[i]
    return suma

def mayor(lista):
    mayor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor

def menor(lista):
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    return menor

def carga():
    lista=[]
    for i in range(5):
        num=int(input("Ingresar numeros: "))
        lista.append(num)
    return lista

lista=carga()
print("El mayor es:",mayor(lista))
print("El menor es: ",menor(lista))
print("Suma del array: ",suma(lista))


def mayor_menor(lista):
    mayor=lista[0]
    menor=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
        else:
            if lista[i]<menor:
                menor=lista[i]

    print("El mayor de la lista es:",mayor," El menor: ",menor)

def cargar():
    lista=[]
    for i in range(5):    
        num=int(input("Ingresar numeros: "))
        lista.append(num)    
    return lista
   
lista1=cargar()
mayor_menor(lista1)

Desempeño 72
• Definir una lista de enteros por asignación en el bloque principal.
Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos.
Mostrar dicho producto en el bloque principal de nuestro programa.

def producto(lista):
    producto=1
    for i in range(len(lista)):
        producto = producto*lista[i]
    return producto
def cargar():
    lista=[]
    for i in range(3):
        numeros=int(input("Ingresar numeros: "))
        lista.append(numeros)
    return lista
lista1=cargar()
print(producto(lista1))


Retornar los números mayores a 10 de una lista
Confeccionar una función que cargue por teclado una lista de 5 enteros
y la retorne. Una segunda función debe recibir una lista y mostrar todos
los valores mayores a 10.
Desde el bloque principal del programa llamar a ambas funciones. 

def cargar():
    lista=[]
    for  i in range(5):
        numeros= int(input("Ingresar numeros: "))
        lista.append(numeros)
    return lista

def mayor(lista):
    lista_mayores=[]
    for i in range(len(lista)):
        if lista[i]>10:
            lista_mayores.append(lista[i])
    return lista_mayores

lista1=cargar()
print(mayor(lista1))

Estructurando nuestras funciones
Confeccionar una función que cargue por teclado una lista de 5 enteros
y la retorne.
Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. Desde el bloque principal del programa llamar a
ambas funciones e imprimir el mayor y el menor de la lista


def cargar():
    lista=[]
    for i in range(5):
        numero=int(input("Ingresar num: "))
        lista.append(numero)
    return lista

def mayor_menor(lista):
    mayor=lista[0]
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
        else:
            if lista[i]<menor:
                menor=lista[i]
    return [mayor,menor]

lista1=cargar()
mayor,menor=mayor_menor(lista1)

print("MAyor",mayor,"Menor",menor)

EJEMPLO 61
Datos cruzados: Detectamos a los mayores de edad y su promedio de edades
Desarrollar un programa que permita cargar 5 nombres de personas y
sus edades respectivas.
Luego de realizar la carga por teclado de todos los datos imprimir los
nombres de las personas mayores de edad (mayores o iguales a 18 años)
Imprimir la edad promedio de las personas.
| Programa: [1]

def cargar():
    nombres=[]
    edades=[]
    for i in range(4):
        name=input("Ingresar nombre: ") 
        nombres.append(name)
        edad=int(input("Ingresar edades: "))
        edades.append(edad)
    return [edades,nombres]
def mayores(lista1,lista2):
    for  i in range(len(lista1)):
        if lista1[i]>=18:
            print("Nombre mayores de edad:",lista2[i],"Edad:",lista1[i])
def promedio(lista):
    promedio=0
    for i in range(len(lista)):
        promedio=promedio+lista[i]
    promedio=promedio//4
    return promedio

lista1,lista2= cargar()
mayores(lista1,lista2)
print(promedio(lista1))

Desempeño 79
| Se tiene que cargar los votos obtenidos por tres candidatos a una elección.En una lista cargar
candidatos=[("juan", [("cordoba",100),("buenos aires",200)]), ("ana", [("cordoba",55)]),("luis", [("buenos aires",20)])]
a| Función para cargar todos los candidatos, sus nombres y las provincias
b| Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.
"
def cargar():
    lista=[]
    for i in range(3):
        name=input("Ingresar nombre: ")
        provincias=int(input("Ingresar cantidad provincias: "))
        for x  in range(provincias):
            provi=input("Ingresar la provi: ")
            votos=int(input("Ingresar votos: "))
            lista.append((name,[(provi,votos)]))
    return lista
def cantidad_votos(lista):
    suma=0
#candidatos=[("juan", [("cordoba",100)]),("ana", [("cordoba",55)]),("luis", [("buenos aires",20)])]
    for i in range(len(lista)):
        suma=0
        for x in range(len(lista[i][1])):
            suma=suma+lista[i][1][x][1]
        print(lista[i][0],suma)

lista1=cargar()
print(lista1)
cantidad_votos(lista1)
EJEMPLO 66
Recorridos para listas y truplas
Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado. Luego en otras funciones:
1) Imprimirla en forma completa.
2) Obtener y mostrar el mayor.
3) Mostrar la suma de todas sus componentes.
Utilizar la nueva sintaxis de for vista en este concepto.


def cargar():
    lista=[]
    for i in range(5):
        numero=int(input("Ingresar numeros: "))
        lista.append(numero)
    return lista
def mayor(lista1):
    mayor=lista1[0]
    for i in lista1:
        if i>mayor:
            mayor=i
    return mayor
def imprimir(lista):
    for i in lista:
        print(i)
lisata1=cargar()
imprimir(lisata1)
print("El mayor es :",mayor(lisata1))

def cargar():
    empleados=[]
    for x in range(3):
        nombre=input("Nombre del empleado:")
        sueldo=int(input("Ingrese el sueldo:"))
        empleados.append((nombre,sueldo))
    return empleados
def imprimir(empleados):
    for nombre,sueldo in empleados:
        print(nombre,sueldo)
def mayor_sueldo(empleados):
   mayor=empleados[1]
   for i in empleados:
       if i[1]>mayor[1]:
           mayor=i
   print(mayor)
lista1=cargar()
print(lista1)
imprimir(lista1)
mayor_sueldo(lista1)

Desempeño 80
| Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.
Desempeño 81
| Almacenar los nombres de 5 productos y sus precios.
Utilizar una lista y cada elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
a| Cargar por teclado.
b| Listar los productos y precios.
c| Imprimir los productos con precios comprendidos entre 10 y 15.

def imprimir(paises):
    for clave in paises:
        print(clave,paises[clave])

paises={"argentina":40000000, "españa":46000000, "brasil":190000000, "uruguay": 3400000}
imprimir(paises)

Diccionario de productos y precios
Crear un diccionario que permita almacenar 5 artículos, utilizar como
clave el nombre de productos y como valor el precio del mismo.
Desarrollar además las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100


def cargar():
    productos={}
    for i in range(3):
        nombre=input("Ingreesar: ")
        precio=int(input("Ingresar valor: "))
        productos[nombre]=precio
    return productos

def mayor(productos):
    for nombre in productos:
        if productos[nombre]>100:
            print(productos[nombre])
productos = cargar()
mayor(productos)

Diccionario de productos y precios
Desarrollar una aplicación que nos permita crear un diccionario inglés/
castellano. La clave es la palabra en ingles y el valor es la palabra en
castellano. Crear las siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario
3) Ingresar por teclado una palabra en ingles y si existe en el diccionario, mostrar su traducción.


def carga():
    diccionario={}
    opcion="si"

    while opcion=="si":
        ingles= input("Ingresar palabra: ")
        espaniol=input("Ingresar palabra en espaniol: ")
        diccionario[ingles]=espaniol
        opcion = input("Ingresar si quiere agragar palabras: ")
    return diccionario

def averiguar(diccionario):
    palabra = input("Que palabra desea saber: ")
    for clave in diccionario:
        if clave== palabra:
            print("La palabra significa:",diccionario[clave])
diccionario=carga()
averiguar(diccionario)

num1=random.randint(1,6)
num2=random.randint(1,6)
suma=num1+num2
if suma==7:
    print("Ganasteeeeeeeeeeeeeeeeeee")
else:
    print("No acerttado")

    EJEMPLO 74
Creador de lista aleatoria y mezcla de elementos
Desarrollar un programa que cargue una lista con 10 enteros.
Cargar los valores aleatorios con números enteros comprendidos entre
0 y 1000. Mostrar la lista por pantalla
"""
def numeros():
    lista=[]
    for i in range(5):
        num =random.randint(1,500)
        lista.append(num)
    return lista

def desornden(lista):
    random.shuffle(lista)
    
lista1=numeros()
print(lista1)
desornden(lista1)
print(lista1)
