valor = int(input())

ano = valor // 365
resto_ano = valor % 365
mes = resto_ano // 30
dias = resto_ano % 30

print(f"{ano} ano (s)")
print(f"{mes} mes (es)")
print(f"{dias} dia (s)")