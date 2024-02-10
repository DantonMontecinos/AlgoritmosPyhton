"""
Desempeño 35
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
"""