import sys
import math
valore = input().split()

R1 = int(valore[0])
X1 = int(valore[1])
Y1 = int(valore[2])
R2 = int(valore[3])
X2 = int(valore[4])
Y2 = int(valore[5])

distancia_centros = math.sqrt((X1 - X2)**2 + (Y1 - Y2)**2)
if distancia_centros + R2 <= R1:
    print("RICO")
else:
    print("MORTO")
