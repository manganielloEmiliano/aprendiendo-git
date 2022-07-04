#Mostrar al ganador (Nro Participante, Nombre, Apellido y Mejor disparo).
def ganador(concurso):
    for item in concurso:
        ganadorId=" "
        mejorDisparo=1000
        if item["mejor disparo"] < mejorDisparo:
            mejorDisparo=item["mejor disparo"]
            ganadorId=item["numeroPart"]
    
    for item in concurso:
        if item["numeroPart"] == ganadorId:
            print("es el ganador!!!")
            print(item)
            break
    return

#Informar quien fue el último (Nro Participante, Nombre, Apellido y Mejor disparo).
def ultimo(concurso):
    
    for item in concurso:
        perdedorId=" "
        peorDisparo=0
        if item["mejor disparo"] > peorDisparo:
            peorDisparo=item["mejor disparo"]
            perdedorId=item["numeroPart"]
    for item in concurso:
        if item["numeroPart"] == perdedorId:
            print("es el ultimo!!!")
            print(item)
            break
    return
#Informar cuantos participantes formaron parte del concurso.
def totalPart(concurso):
    totalp=0
    for item in concurso:
        totalp=totalp +1
    return totalp
#Informar cuantos hombres formaron parte del concurso
def numeroM(concurso):
    numeroM=0
    for item in concurso:
        if item["sexo"]=="m" or item["sexo"]=="M":
            numeroM=numeroM+1
    return numeroM
#Informar edad promedio de las mujeres
def edadPm(concurso):
    edadPmV=0
    totalF=totalPart(concurso)-numeroM(concurso)
    
    for item in concurso:
        if item["sexo"]=="f" or item["sexo"]=="F":
            edadPmV=(edadPmV + item["edad"])
            
    return edadPmV/totalF
#Informar el promedio de todos los disparos.
def Dpromedio(concurso):
    disparos=0
    contador=0
    for item in concurso:
        disparos=disparos +item["disparo1"]+item["disparo2"]
        contador=contador+2
    return disparos/contador    

        
            
    