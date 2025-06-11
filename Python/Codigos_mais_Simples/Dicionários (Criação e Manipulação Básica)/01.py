aluno = {
    "nome": "Jack",
    "idade": 20,
    "curso": "Engenharia de Software"
}
print(f"Seu nome {aluno['nome']}, idade {aluno['idade']} e o seu curso {aluno['curso']}.")
print(aluno["curso"])
aluno["idade"] = 21
print(f"Sua idade foi modificada {aluno['idade']}")
aluno['cidade'] = "Belo Horizonte."
print(aluno)

if "email" in aluno:
    print("A chave 'email' existe no dicionario.")
else:
    print("A chave 'email' não existe!")