import random
#from random import randint
#import random as rn
n = random.randint(1, 101)
print n

adivinado=False

for i in range(5):
	a=input("Prueba tu suerte, ingresa un valor: ")
	if a==n:
		print "Felicidades, ganaste"
		adivinado=True
		break
	elif a < n:
		print "El valor que ingresaste es menor"
	elif a > n:
		print "El valor que ingresaste es mayor"

if not adivinado:
	print "El valor que debias adivinar era: " + str(n)