def calcular_duracao_evento():
    
    dia_inicial_str = input().split()
    dia_inicial = int(dia_inicial_str[1])

    hora_inicial, minuto_inicial, segundo_inicial = map(int, input().split(' : '))

    dia_final_str = input().split()
    dia_final = int(dia_final_str[1])

    hora_final, minuto_final, segundo_final = map(int, input().split(' : '))

    total_dias = dia_final - dia_inicial
    total_horas = hora_final - hora_inicial
    total_minutos = minuto_final - minuto_inicial
    total_segundos = segundo_final - segundo_inicial

    if total_segundos < 0:
        total_segundos += 60
        total_minutos -= 1

    if total_minutos < 0:
        total_minutos += 60
        total_horas -= 1
    
    if total_horas < 0:
        total_horas += 24
        total_dias -= 1

    print(f"{total_dias} dia(s)")
    print(f"{total_horas} hora(s)")
    print(f"{total_minutos} minuto(s)")
    print(f"{total_segundos} segundo(s)")

calcular_duracao_evento()