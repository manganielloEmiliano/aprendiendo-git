nombre = input("ingrese su nombre: ")#se ingresa el nombio#
edad = int(input("ingrese su edad: "))#el usuario ingresa edad ,se pone int ,para que transforme el string en entero#

print("hola {} buenos dias ,tu edad es {}".format(nombre,edad))

#calcular el perimetro de un rectangulo#
base = float(input("ingresar la base del rectangulo: "))#convierte el string en numero real
altura = float(input("ingresar la altura del rectangulo: "))
perimetro = (base + altura)* 2
print("el valor del perimetro es: {}".format(perimetro))


#dados los catetos de un triangulo,calcular la hipotenusa"
from math import sqrt#importar raiz cuadrada#
cateto1 = int(input("ingrese el cateto 1 : "))
cateto2 = int(input("ingrese el cateto 2 :")) 
hipotenusa = sqrt(cateto1*cateto1 +cateto2*cateto2)#se puede usar ** para hacer la potencia#
print("el valor de la hipotenusa es: {}".format(hipotenusa))