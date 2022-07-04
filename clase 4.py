cantidad = int(input("ingresar cantidad = "))
precio =  float(input("ingresar valor de producto ="))
descuento = 0

if cantidad > 0:
    if cantidad > 20:
        descuento = 10
    else:
        if cantidad <= 20 and cantidad >0 :
            descuento = 5
        else:
            descuento = 0
        
    valor_a_descontar = precio * cantidad *descuento/100
    valor_a_pagar =precio*cantidad-valor_a_descontar    
    print("debe pagar{} pesos".format(valor_a_pagar))
else:    
    print("ingrese valores mayores a 0")        