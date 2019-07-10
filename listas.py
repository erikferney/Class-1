valores=[1,2,3,4,5]
print valores
print valores[1]
print valores[-1]
print valores[1:-1]
new_valor=input("Ingrese nuevo valor: ")
valores+=[new_valor]
print valores
valores.append(new_valor)
print valores
valores.append(input("Ingrese otro valor: "))
print valores
valores.pop(0)
print valores
n=0
m=0
for i in valores:
    if i % 2 == 0:
        n = n + i
    else:
        m = m + i

print "La suma de numeros pares es: " + str(n)
print "La suma de numeros impares es: " + str(m)
