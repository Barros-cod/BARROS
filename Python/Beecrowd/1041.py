valores = input().split()

x = float(valores[0])
y = float(valores[1])

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
else:
    print("Origem")
