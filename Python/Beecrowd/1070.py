X = int(input())

contador_impares = 0

while contador_impares < 6:
    if X % 2 != 0:
        print(X)
        contador_impares += 1

    X += 1

input("")