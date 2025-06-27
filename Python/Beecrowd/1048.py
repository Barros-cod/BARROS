valor = float(input())

if valor <= 400:
    percentual = 15
    reajuste_ganho = (percentual /100) * valor
elif valor <= 800:
    percentual = 12
    reajuste_ganho = (percentual /100) * valor
elif valor <= 1200:
    percentual = 10
    reajuste_ganho = (percentual /100) * valor
elif valor <= 2000:
    percentual = 7
    reajuste_ganho = (percentual /100) * valor
elif valor > 2000:
    percentual = 4
    reajuste_ganho = (percentual /100) * valor

novo_valo = reajuste_ganho + valor

print(f"Novo salario: {novo_valo:.2f}")
print(f"Reajuste ganho: {reajuste_ganho:.2f}")
print(f"Em percentual: {percentual} %")