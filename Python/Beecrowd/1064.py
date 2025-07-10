total = 0
valores_positivos = 0

for i in range(6):
    numero = float(input())

    if numero > 0:
        total += numero 
        valores_positivos += 1

print(f"{valores_positivos} valores positivos")
print(total / valores_positivos)
input()