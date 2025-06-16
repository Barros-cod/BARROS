nome_vendedor = input("")
salario_fixo = float(input())
suas_vendas = float(input())

total = (15/100) * suas_vendas

print(f"TOTAL = R$ {total + salario_fixo:.2f}")