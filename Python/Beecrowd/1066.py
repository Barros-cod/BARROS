quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0

for i in range(5):
    numero = int(input())

    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1
    
    if numero > 0:
        quantidade_positivos += 1

    if numero < 0:
        quantidade_negativos += 1

print(f"{quantidade_pares} valor(es) par(es)")
print(f"{quantidade_impares} valor(es) ímpar(es)")
print(f"{quantidade_positivos} valor(es) positivo(s)")
print(f"{quantidade_negativos} valor(es) negativo(s)")