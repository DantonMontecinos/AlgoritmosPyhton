"""
Desempeño 14
• Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos
valores enteros x e y (distintos a cero).
Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto.
(1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
"""

ejex = int(input("Ingrese eje x: "))
ejey = int(input("Ingrese eje y: "))


if ejex!=0 and ejey!=0:
    print("Distintos de cero")
    if ejex>0 and ejey>0:
        print(str(ejex)+","+str(ejey)+"="+" Cuadrante 1")
    elif ejex>0 and ejey<0:
        print(str(ejex)+","+str(ejey)+"="+" Cuadrante 4")
    elif ejex<0 and ejey>0:
        print(str(ejex)+","+str(ejey)+"="+" Cuadrante 2")
    else:
        print(str(ejex)+","+str(ejey)+"="+" Cuadrante 3")
else:
    print("se detectó un ceroooo")
    if ejex==0:
        print("Ejex= "+str(ejex))
    else:
        print("Ejey= "+str(ejey))