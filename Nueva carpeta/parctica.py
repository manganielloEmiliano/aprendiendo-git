"""El programa debe realizar lo siguiente:
a)Por cada participante, el programa debe permitir el ingreso de los siguientes datos:
b)Número único del participante.
c)Nombre y Apellido del participante.
d)Edad del participante.
e)Sexo del participante.
f)Disparo. Solo almacenar la distancia al origen.
g)El fin de ingreso de participantes se determina ingresando con número de participante igual a 999.
"""
from funciones import ganador,ultimo,totalPart,numeroM,edadPm,Dpromedio
cantPart=0
concurso=[]
while True:
    numeroPart= int(input("ingrese el numero de participantes: "))
    #g)El fin de ingreso de participantes se determina ingresando con número de participante igual a 999.
    if numeroPart==999:
        break
    nombre= str(input("ingrese el nombre del participante : "))  
    apellido= str(input("ingrese el apellido del participante : "))
    edad=int(input("ingrese la edad del participante = "))
    sexo=str(input("ingrese sexo f/M : "))  
    disparo1= float(input("ingrese la distancia al origen del disparo = "))
    disparo2= float(input("ingrese la distancia al origen del disparo = "))
    cantPart=cantPart+1
    
    datos={
        "numeroPart": " " ,
          "nombre": " ",
          "apellido": " ",
          "edad": " ",
          "sexo":" ",
          "disparo1": " ",
          "disparo2": " ",
          "mejor disparo": " "}
    datos["numeroPart"] = numeroPart
    datos["nombre"] =nombre
    datos["apellido"]=apellido
    datos["edad"]=edad
    datos["sexo"] =sexo
    datos["disparo1"]=disparo1    
    datos["disparo2"]=disparo2 
    
    if disparo1 <disparo2:
        datos["mejor disparo"]=disparo1
    else:
        datos["mejor disparo"]=disparo2
        
    concurso.append(datos)
print(concurso)  
#Mostrar al ganador (Nro Participante, Nombre, Apellido y Mejor disparo)  
ganador(concurso)
#Informar quien fue el último (Nro Participante, Nombre, Apellido y Mejor disparo).
ultimo(concurso)
#Informar cuantos participantes formaron parte del concurso.
print("el total de participantes fue ",totalPart(concurso))
#Informar cuantos hombres formaron parte del concurso
print("los participantes hombres fueron ",numeroM(concurso))
#Informar edad promedio de las mujeres
print("la edad promedio de las mujeres participantes es de ",edadPm(concurso))
#Informar el promedio de todos los disparos.
print("el promedio de todos los disparos es de ",Dpromedio(concurso))


