peca1 = input("").split()
peca2 = input("").split()

numero0 = float(peca1[1])
numero1 = float(peca1[2])

numero2 = float(peca2[1])
numero3 = float(peca2[2])

valor_pagar = (numero0 * numero1) + (numero2 * numero3)

print(f"VALOR A PAGAR: R$ {valor_pagar:.2f}")

