"""
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

Desempeño 70
• Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un
segundo parámetro de tipo entero.
Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.
lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)



def multiplicar(lista,n):
    
    for i in range(len(lista)):
        print(lista[i],"*",n,":",lista[i]*n)

lista=[3, 7, 8, 10, 2]
num=int(input("ingresar num: "))
multiplicar(lista,num)

Desempeño 71
• Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres.
Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja. 
En el bloque principal iniciamos por asignación la lista de string:

print("Palabra con mas caracteres:",mascaracteres(palabras)))

def guardar_posicion(lista):
    posicion=0
    mayor=len(lista[0])   
    for i in range(1,len(lista)):    
        if len(lista[i])>mayor:
            mayor=len(lista[i])
            posicion=i        
    return posicion

def mascaracteres(lista):    
    mayor=len(lista[0])   
    for i in range(1,len(lista)):    
        if len(lista[i])>mayor:
            mayor=len(lista[i])         
    return mayor
fechas=["enero", "febrero", "marzo", "abril", "mayooooo", "junio"]

print("La palabra mayor es: ",fechas[(guardar_posicion(fechas))],"con:",mascaracteres(fechas))

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

Desempeño 73
• En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
a| Carga de los sueldos en una lista.
b| Impresión de todos los sueldos.
c| Cuántos tienen un sueldo superior a $4000.
d| Retornar el promedio de los sueldos.
e| Mostrar todos los sueldos que están por debajo del promedio

def cargar():
    lista=[]
    for i in range(5):
        sueldos=int(input("Ingresar sueldos: "))
        lista.append(sueldos)
    return lista

def sueldo_superior(lista):
    contador=0
    for i in range(len(lista)):
        if lista[i]>4000:
            contador+=1
    return contador
def promedio(lista):
    promedio=0
    for i in range(len(lista)):
        promedio=promedio+lista[i]
    promedio=promedio//5
    return promedio

def bajo_promedio(lista,prom):
    contador=0
    for i in range(len(lista)):
        if lista[i]<prom:
            contador+=1
    return contador

lista1=cargar()
print(lista1)
print("Sueldos superior a 4000:",sueldo_superior(lista1))
prom = promedio(lista1)
print("Promedio de sueldos:",prom)
print("Sueldos bajo el promedio: ",bajo_promedio(lista1,prom))

Desempeño 74
• Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus
precios. Definir las siguientes funciones:
a| Cargar los nombres de artículos y sus precios.
b| Imprimir los nombres y precios.
c| Imprimir el nombre de artículo con un precio mayor
d| Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor
igual al valor ingresado



def cargar():
    articulos=[]
    precios=[]
    for  i in range(4):
        names=input("Ingresar productos: ")
        articulos.append(names)
        p = int(input("Ingresar precio: "))
        precios.append(p)
    
    return [articulos,precios]


def precio_mayor(lista):
    mayor=lista[0]
    pos=0
    for i in range(len((lista))):
        if lista[i]>mayor:
            mayor=lista[i]
            pos=i
    print(mayor)
    return pos

def importe_menor(lista2):
    contador=0
    importe=int(input("Ingresar importe: "))
    for i in range(len(lista2)):
        if lista2[i]<=importe:
            contador+=1
    return contador

lista1,lista2 = cargar()
print(lista1,lista2)
print("El producto con amyor precio es: ",lista1[precio_mayor(lista2)])
print("Porductos con un valor menor a improte ingresado",importe_menor(lista2))
print(lista2)

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

"""