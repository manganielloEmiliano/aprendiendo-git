def ganador(concurso):
    for item in concurso:
        ganadorId=""
        mejorDisparo=9999999999999999999
        if item["mejor disparo"]< mejorDisparo:
            mejorDisparo=item["mejor disparo"]
            ganadorId=item["numeroPart"]
    for item in concurso:
        if item ==ganadorId:
            print("es el ganador!!!")
            print("item")
            break
    return
    
    
    
