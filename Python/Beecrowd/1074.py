n = int(input())

for i in range(n):
    valores = int(input())
    if valores == 0:
        print("NULL")
    elif valores % 2 == 0:
        valor = "EVEN" 
    elif valores % 2 != 0:
        valor = "ODD"
    if valores > 0:
        print(f"{valor} POSITIVE")
    elif valores < 0:
        print(f"{valor} NEGATIVE")
        
