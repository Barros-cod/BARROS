valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

lados = sorted([a, b, c], reverse=True)
a = lados[0] 
b = lados[1]
c = lados[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif (a ** 2 == b ** 2 + c ** 2):
    print("TRIANGULO RETANGULO")
elif (a ** 2 > b ** 2 + c ** 2):
    print("TRIANGULO OBTUSANGULO")
elif (a ** 2 < b ** 2 + c ** 2):
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or a == c or b == c:
    print("TRIANGULO ISOSCELES")