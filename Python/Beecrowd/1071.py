x = int(input())
y = int(input())

soma_impares = 0

if x < y:
    menor = x
    maior = y
else:
    menor = y
    maior = x

for numero in range(menor + 1, maior):
    if numero % 2 != 0:
        soma_impares += numero

print(soma_impares)