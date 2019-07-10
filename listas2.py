valores=range(101)#iria desde 0 hasta 100
print valores
valores2=range(50, 101)#iria desde 50 hasta 100
print valores2
valores3=range(50, 101, 2)#iria desde 50 hasta 100 de 2 en 2
print valores3
n=0
m=0
for i in valores:
    if i % 2 == 0:
        n = n + i
    else:
        m = m + i

print "La suma de numeros pares es: " + str(n)
print "La suma de numeros impares es: " + str(m)
