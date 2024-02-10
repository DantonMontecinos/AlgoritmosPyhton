"""
Desempeño 75
• Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus
precios. Definir las siguientes funciones:
a| Cargar los nombres de artículos y sus precios.
b| Imprimir los nombres y precios.
c| Imprimir el nombre de artículo con un precio mayor
d| Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor
igual al valor ingresado.

def precio_mayor(articulos,precios):
    may=precios[0]
    pos=0
    for x in range(1,len(precios)):
        if precios[x]>may:
            may=precios[x]
            pos=x
    print("Articulo con un precio mayor es :",articulos[pos],"su precio es:",may)

def carga():
    articulos=[]
    precios=[]
    for i in range(3):
        names= input("Ingresar nombre articulo: ")
        articulos.append(names)
        prices=int(input("Ingrese el precio: "))
        precios.append(prices)
    return [articulos,precios]

articulos,precios=carga()
print(articulos,precios)
precio_mayor(articulos,precios)

def carga():
    dia=int(input("Cargar dia: "))
    mes=int(input("Cargar mes : "))
    anio=int(input("Cargar anio: "))

    return(dia,mes,anio)
fecha = carga()
print(fecha)

list(fecha)
print(fecha)

EJEMPLO 64
Conversión de datos
Definir una tupla con tres valores enteros. Convertir el contenido de la
tupla a tipo lista. Modificar la lista y luego convertir la lista en tupla.
| Programa: [3]


tupla = (2,5,7,10)

conver=list(tupla)
conver.append(17)
tupla2=tuple(conver)
print(tupla2)

Empaquetado y desempaquetado de tuplas.
Podemos generar una tupla asignando a una variable un conjunto de
variables o valores separados por coma:

| El desempaquetado de la tupla "fecha" se produce cuando definimos
tres variables separadas por coma y le asignamos una tupla:
dd,mm,aa=fecha

fecha = (21,4,1995)
d,m,a = fecha

print("Dia:",d,"Mes:",m,"Anio:",a)

Desempeño 76
Problema en la fiesta: Confeccionar un programa con las siguientes funciones:
a| Cargar una lista de 5 enteros.
b| Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
 
def mayor_menor(lista):
    mayor=lista[0]
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
        else:
            if lista[i]<menor:
                menor=lista[i]
    return (mayor,menor)
lista=[44,550,60,100,4]
mayor,menor = mayor_menor(lista)
print(lista)
print("Numero mayor",mayor)
print("Numero menor: ",menor)

Desempeño 77
| Confeccionar un programa con las siguientes funciones:
a| Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores.
b| Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados
y muestre el nombre del empleado con sueldo mayor. En el bloque principal del programa llamar
dos veces a la función de carga y seguidamente llamar a la función que muestra el nombre de empleado con sueldo mayor.
# bloque principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)


def cargar_datos():
    nombre=input("Ingresar nombre: ")
    sueldo=int(input("Ingresar sueldo: "))
    return (nombre,sueldo)
def mayor_sueldo(tupla1,tupla2):
    if empleado1[1]>empleado2[1]:
        print(empleado1[0],"Mayor salario")
    else:
        print(empleado2[0],"MAyor salario")
empleado1 = cargar_datos()
empleado2=cargar_datos()

mayor_sueldo(empleado1,empleado2)

EJEMPLO 65
Almacén de habitantes por países
Almacenar en una lista de 5 elementos tuplas que guarden el nombre de
un país y la cantidad de habitantes.
Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y 
en la tercera mostrar el nombre del país con mayor cantidad
de habitantes.


def mayor(lista):
    pos=0
    for i in range(len(lista)):
        if lista[i][1]>lista[pos][1]:
            pos=i
    print("Mayor cantidad habitantes: ",lista[pos][0])


def cargar():
    lista=[]
    for i in range(3):
        pais=input("Ingresa pais: ")
        habitantes=int(input("Ingresar habitantes: "))
        lista.append((pais,habitantes))
    return lista
def imprimir(lista):
    for i in range(len(lista)):
        print(lista[i])

datos = cargar()
info = imprimir(datos)
mayor(datos)

Desempeño 78
| Almacenar en una lista de 5 elementos los nombres de empleados de una empresa junto a sus
últimos tres sueldos (estos tres valores en una tupla)
El programa debe tener las siguientes funciones:
a| Cargar una lista de 10 elementos enteros.
b| Imprimir el monto total cobrado por cada empleado.
c| Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en
los últimos tres meses.




def cargar():
    lista=[]
    for i in range(3):
        nombres=input("Ingresar nombres: ")
        sueldo1=int(input("Ingresar sueldo1: "))
        sueldo2=int(input("Ingresar sueldo2: "))
        sueldo3=int(input("Ingresar sueldo3: "))

        lista.append([nombres,(sueldo1,sueldo2,sueldo3)])

    return lista
def total_empleado(lista):
    suma=0
    for i in range(len(lista)):
        suma=lista[i][1][0]+lista[i][1][1]+lista[i][1][2]
        print("Total",lista[i][0],suma)
    return suma
def mayor_diezmil(lista):
    for i in range(len(lista)):
        total = lista[i][1][0]+lista[i][1][1]+lista[i][1][2]
        if total > 100000:
            print("Suedlos  mayor a 10,000: ",lista[i][0],total)


lista=cargar()
print(lista)
total=total_empleado(lista)
print(total)
mayor_diezmil(lista)

DESEMPEÑO 79
| Se tiene que cargar los votos obtenidos por tres candidatos a una elección.En una lista cargar
en la primer componente el nombre del candidato y en la segunda componente cargar una lista
con componentes de tipo tupla con el nombre de la provincia y la cantidad de votos obtenidos en
dicha provincia. Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría
una estructura similar a esta:
candidatos=[("juan", [("cordoba",100),("buenos aires",200)]), ("ana", [("cordoba",55)]),
("luis", [("buenos aires",20)])]

a| Función para cargar todos los candidatos, sus nombres y las provincias
b| Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.


def totalvotos_candidato(candidatos):
    for x in range(len(candidatos)):
        suma=0
        for z in range(len(candidatos[x][1])):

            suma=suma+candidatos[x][1][z][1]
        print(candidatos[x][0],suma)

def cargar():
    lista=[]
    for i in range(3):
        candidato=input("Ingresar candidato: ")
        provincia=input("Ingresa provincia: ")
        votos=int(input("Ingresar cantidad votos: "))
        lista.append(((candidato),[(provincia,votos)]))
    return lista

lista=cargar()
totalvotos_candidato(lista)

"""