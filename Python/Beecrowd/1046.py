horas_inical, horas_final = map(int, input().split())

duracao = 0

if horas_inical < horas_final:
    duracao = horas_final - horas_inical
elif horas_inical >= horas_final:
    duracao = (24 - horas_inical) + horas_final

if duracao == 0:
    duracao = 24

print(f"O JOGO DUROU {duracao} HORA(S)")