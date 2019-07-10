import random
#from random import randint
#import random as rn

lista = []

for i in range(3):
	lista.append(random.randint(1,101))
	
print lista

adivinado=False

for i in range(5):
	a=input("Prueba tu suerte, ingresa un valor: ")
	if a in lista:
		print "Felicidades, ganaste"
		adivinado=True
		break
	else:
		print "Sigue intentando"

if not adivinado:
	cadena = ""
	
	for i in lista:
		if cadena <> "":
			cadena += ","
		
		cadena += str(i)

print "El valor que debias adivinar era: " + cadena #o se podría sumar todo con la coma y mostrar cadena[:-2]