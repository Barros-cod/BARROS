# Criando um conjunto
cores_favorita = { "azul", "verde", "vermelho", "azul"}
print(cores_favorita)

cores_favorita.add("amarelo")
cores_favorita.add("verde")
cores_favorita.remove("vermelho")
print(cores_favorita)

cores_segundarias = {"verde", "roxo", "laranja"}
conjunto = cores_favorita.intersection(cores_segundarias)
print(conjunto)

union = cores_favorita.union(cores_segundarias)
print(union)

















