positivos = 0
valores = []

for i in range(6):
    valor = float(input(""))
    valores.append(valor)
    if valor > 0:
        positivos += 1

print(f"{positivos} valores positivos")

input("")