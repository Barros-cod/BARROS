maior_valor = 0
posicao_maior = 0

for i in range(1, 101):
    valor_atual = int(input())

    if valor_atual > maior_valor:
        maior_valor = valor_atual
        posicao_maior = i

print(maior_valor)
print(posicao_maior)