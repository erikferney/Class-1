import random
#from random import randint
#import random as rn

lista = []
#valores=[x for x in randint(0,9) if not x in valores]
for i in range(10):
	item = random.randint(0,9)
	
	if not item in lista:
		lista.append(item)
	
	if len(lista) == 3:
		break
	
print lista

adivinado=False

for i in range(5):
	a=raw_input("Prueba tu suerte, ingresa un valor de no mas de tres caracteres: ")
	
	if len(a) <> 3:
		print "La longitud maxima de la cadena es de tres digitos"
		break
		
	indice = 0
	picas = 0
	fijas = 0

	while indice < len(a):
		if lista[indice]==int(a[indice]):
			fijas += 1
		elif int(a[indice]) in lista:
			picas += 1
		
		indice += 1
	
	if fijas == len(a):
		print "Felicidades, has obtenido todas las fijas"
		break
	else:
		print "Obtuviste " + str(fijas) + " fijas y " + str(picas) + " picas"
		
