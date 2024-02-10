"""
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

Desempeño 57
• Se desea saber la temperatura media trimestral de cuatro países.
Para ello se tiene como dato las temperaturas medias mensuales de dichos países.
| Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
| Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
a| Cargar por teclado los nombres de los países y las temperaturas medias mensuales.
b| Imprimir los nombres de las países y las temperaturas medias mensuales de las mismas.
c| Calcular la temperatura media trimestral de cada país.
d| Imprimir los nombres de los países y las temperaturas medias trimestrales.
e| Imprimir el nombre del país con la temperatura media trimestral mayor.

paises = []
temperaturas =[[],[],[],[]]
promedios=[]

for i in range(4):
    input_paises = input("Ingrese paises: ")
    paises.append(input_paises)    
    for x in range(3):
        temp = int(input("Ingrese las temperaturas: "))
        temperaturas[i].append(temp)

promedios=[]
for k in range(4):
    prom = (temperaturas[k][0] +temperaturas[k][1]+temperaturas[k][2])//3
    promedios.append(prom)
print(paises)
print(temperaturas)
print(promedios)


Desempeño 58
• Definir una lista y almacenar los nombres de 3 empleados.
| Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de
días del mes que el empleado faltó. Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.

empleados=[]
dias_falta=[]

for i in range(3):
    em=input("Ingresar empleado: ")
    empleados.append(em)
    dias_falta.append([])
    faltas=int(input("Ingresar cuantos dias faltó: "))
    for x in range(faltas):
        dias=int(input("Ingresar dias que faltó: "))
        dias_falta[i].append(dias)

for x in range(len(dias_falta)):
    print(empleados[x],len(dias_falta[x]))
print(empleados)
print(dias_falta)


Desempeño 59
• Desarrollar un programa que cree una lista de 50 elementos.
El primer elemento es una lista con un elemento entero, el segundo elemento es una lista de dos
elementos etc.
| La lista debería tener la siguiente estructura y asignarle esos valores a medida que se crean
los elementos:
[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]


lista=[]
for i in range(1,51):
    lista.append([])
for x in range(len(lista)):
    for i in range(x+1):
        lista[x].append(i+1)
print(lista)
print(len(lista))


Desempeño 60
• Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los
sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como
su nombre)

empleado=[]
sueldos=[]
for  i in range(3):
    nam=input("Ingresar empleados: ")
    s=int(input("Ingresar sueldo: "))
    empleado.append(nam)
    sueldos.append(s)
pos=0
print(empleado)
print(sueldos)
posicion=0
while posicion<len(sueldos):
    if sueldos[posicion]>10000:
        sueldos.pop(posicion)
        empleado.pop(posicion)
    else:
        posicion=posicion+1
print(empleado)
print(sueldos)

Desempeño 61
• Crear una lista de 5 enteros y cargarlos por teclado.
Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.

lista=[]
for i in range(5):
    n=int(input("Ingresar numeros: "))
    lista.append(n)
print(lista)
pos=0

while pos<len(lista):
    if lista[pos]>=10:
        lista.pop(pos)
    else:
        pos+=1
print(lista)


"""