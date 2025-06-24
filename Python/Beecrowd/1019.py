valor = int(input())
# horas:minutos:segundos
horas = valor // 3600
restante_horas = valor % 3600
minutos = restante_horas // 60
segundos = restante_horas % 60

print(f"{horas}:{minutos}:{segundos}")