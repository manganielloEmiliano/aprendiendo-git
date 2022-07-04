"""El programa debe realizar lo siguiente:
a)Por cada participante, el programa debe permitir el ingreso de los siguientes datos:
b)Número único del participante.
c)Nombre y Apellido del participante.
d)Edad del participante.
e)Sexo del participante.
f)Disparo. Solo almacenar la distancia al origen.
g)El fin de ingreso de participantes se determina ingresando con número de participante igual a 999.
"""
import ganador from funciones
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
          "disparo1": " ",
          "disparo2": " ",
          "mejor disparo": " ",}
    datos["numeroPart"] = numeroPart
    datos["nombre"] =nombre
    datos["apellido"]=apellido
    datos["edad"]=edad
    datos["disparo1"]=disparo1    
    datos["disparo2"]=disparo2 
    
    if disparo1 <disparo2:
        datos["mejor disparo"]=disparo1
    else:
        datos["mejor disparo"]=disparo2
        
    concurso.append(datos)
print(concurso)    

