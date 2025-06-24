valor = float(input())

print("NOTAS:")
notas = [100, 50, 20, 10, 5, 2]
for nota in notas:
    quantidade_notas = valor // nota
    print(f"{quantidade_notas} nota(s) de R$ {nota:.2f}")
    valor %= nota

print("MOEDAS:")
moedas = [100, 50, 25, 10, 5, 1]
for moeda in moedas:
    quantidade_notas = valor // moeda
    print(f"{quantidade_notas} nota(s) de R$ {moeda / 100:.2f}")
    valor %= moeda