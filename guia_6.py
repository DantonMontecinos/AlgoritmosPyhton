"""
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


Desempenio #47
#Crear y cargar dos listas con los
#nombres de 5 productos en una y sus respectivos precios en
#otra. Definir dos listas paralelas.
#Mostrar cuántos productos tienen un precio mayor al primer
#producto ingresado.

lista1=["pc","teleofono","iphone","auriculares","termo"]
lista2=[1500,3500,2500,900,600]

producto=lista2[0]
mayores=0
for i in lista2:
    if i>producto:
        mayores+=1

print(lista1)
print(lista2)

print("Productos mayores al primero: "+str(mayores))


DESEMPENIO #48
#En un curso de 4 alumnos se registraron las notas de sus exámenes y
#se deben procesar
#de acuerdo a lo siguiente:
#a| Ingresar nombre y nota de cada alumno
#(almacenar los datos en dos listas paralelas)
#b| Realizar un listado que muestre los nombres, notas
#y condición del alumno. En la condición,
#colocar "Muy Bueno" si la nota es mayor o igual a 8, 
#"Bueno" si la nota está entre 4 y 7, y colocar
#"Insuficiente" si la nota es inferior a 4.
#c| Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”

lista1=["Cole","Lia","Marti","Luli"]
lista2=[2,5,9,4]
muy_bueno=0
bueno=0
insuficiente=0

for i in lista2:
    if i>=8 and i<=10:
        muy_bueno+=1 
    else:
        if i>=4 and i>=7:
            bueno+=1
        else:
            insuficiente+=1
for i in lista2:
    if i==2:
        lista1[0]="Cole: Insuficiente"
    else:
        if i==5:
            lista1[1]="Lia: Bueno"
        if i==9:
            lista1[2]="Marti: Muy bueno"
        else:
            lista1[3]="Luli: Bueno"

print(lista1)
print(lista2)
print("Alumnos muy buenos: "+str(muy_bueno))



Desempeño 49
• Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada
una. Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada
lista. Mostrar esta tercer lista


lista_1=[]
lista_2=[]
lista_3=[]

for i in range(4):
    num = int(input("Ingresar num: "))
    lista_1.append(num)
for x in range(4):
    num = int(input("Ingresar num_lista_2: "))
    lista_2.append(num)
print(lista_1)
print(lista_2)

for y in range(len(lista_1)):

    suma = lista_1[y]+lista_2[y]
    lista_3.append(suma)
print(lista_3)

"""