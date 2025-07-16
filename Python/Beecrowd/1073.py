valor = int(input())

for i in range(1, valor + 1):
    if i % 2 == 0:
        y = i**2
        print(f"{i}^2 = {y}.")