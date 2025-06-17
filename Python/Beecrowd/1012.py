tres_valores = input("").split()

p0 = float(tres_valores[0])
p1 = float(tres_valores[1])
p2 = float(tres_valores[2])

triangulo = p0 * p2 / 2
circulo = 3.14159 * p2 ** 2
trapezio = (p0 + p1) * p2 / 2
quadrado = p1 * 4
retangulo = p0 * p1

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")