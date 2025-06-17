import math

dois_valores = input("").split()
outro_valores = input("").split()

x0 = float(dois_valores[0])
y0 = float(dois_valores[1])

x1 = float(outro_valores[0])
y1 = float(outro_valores[1])

soma_distancia = ((x1 - x0) ** 2) + ((y0 - y1) ** 2)
distancia = math.sqrt(soma_distancia)

print(f"{distancia:.4f}")