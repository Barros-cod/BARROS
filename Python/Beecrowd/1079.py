n = int(input())

for i in range(n):
    a, b, c = map(float, input().split())
    
    peso_a = 2
    peso_b = 3
    peso_c = 5

    media = (a * peso_a + b * peso_b + c * peso_c) / (peso_a + peso_b + peso_c)

    print(f'{media:.1f}')