tres_valores = input("").split()

p0 = float(tres_valores[0])
p1 = float(tres_valores[1])
p2 = float(tres_valores[2])

maior_entre_p0_p1 = (p0 + p1 + abs(p0 - p1)) / 2

maior_final = (maior_entre_p0_p1 + p2 + abs(maior_entre_p0_p1 - p2)) / 2
print(f"{maior_final} eh o maior")