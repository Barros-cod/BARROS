valores = input().split()

numeros = []
numeros_ordenados = []

for i in valores:
    numeros.append(int(i))
    numeros_ordenados.append(int(i))

numeros_ordenados.sort()

for t in numeros_ordenados:
    print(t)

print("")

for n in numeros:
    print(n)