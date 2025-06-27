valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if (a + b > c) and (a + c > b) and (b + c > a):
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")