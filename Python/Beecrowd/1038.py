valores = input().split()

a = int(valores[0])
b = int(valores[1])

cachorro = 4.00
salada = 4.50
bacon = 5.00
torrada = 2.00
refrigerante = 1.50

if 1 == a:
    soma = cachorro * b
elif 2 == a:
    soma = salada * b
elif 3 == a:
    soma = bacon * b
elif 4 == a:
    soma = torrada * b
elif 5 == a:
    soma = refrigerante * b

print(f"Total: R$ {soma:.2f}")