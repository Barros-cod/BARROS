horas_inicial, minuto_inicial, horas_final, minuto_final  = map(int, input().split())

minutos_inicial_total = (horas_inicial * 60) + minuto_inicial
minuto_final_total = (horas_final * 60) + minuto_final

if minuto_final_total > minutos_inicial_total:
    duracao = minuto_final_total - minutos_inicial_total
elif minuto_final_total <= minutos_inicial_total:
    duracao = (24 * 60 - minutos_inicial_total) + minuto_final_total

horas_duracao = duracao // 60
minutos_duracao = duracao % 60
print(f"O JOGO DUROU {horas_duracao} HORA(S) E {minutos_duracao} MINUTO(S)")