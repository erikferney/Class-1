valores=[x**2 for x in range(1, 101)]
print valores

valores=[x**2 for x in range(1, 101, 2)]
print valores

valores=[x**2 for x in range(5, 101, 5)]
print valores

valores=[x**2 for x in range(1, 101) if x%5==0]
print valores

valores=[x for x in range(1,101) if x%2==0]
print len(valores)

valores=[x for x in range(1,101) if x%2==0]
print sum(valores)
