valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
d = float(valores[3])

peso_a = 2
peso_b = 3
peso_c = 4
peso_d = 1

media = (a * peso_a + b * peso_b + c * peso_c + d * peso_d) / (peso_a + peso_b + peso_c + peso_d)

if media >= 7.0:
    print(f"Media: {media:.1f}")
    print(f"Aluno aprovado.")
elif 5.0 <= media <= 6.9: 
    print(f"Media: {media:.1f}")
    print(f"Aluno em exame.")
    
    nota_exame = float(input()) 
    print(f"Nota do exame: {nota_exame:.1f}")
    
    media_final = (nota_exame + media) / 2
    
    if media_final >= 5.0:
        print(f"Aluno aprovado.")
        print(f"Media final: {media_final:.1f}")
    else:
        print(f"Aluno reprovado.")
        print(f"Media final: {media_final:.1f}")
else: 
    print(f"Media: {media:.1f}")
    print(f"Aluno reprovado.")