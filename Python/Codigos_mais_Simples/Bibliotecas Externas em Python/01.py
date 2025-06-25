# Importantando biblioteca que faz requisições web:
import requests

# Fazendo uma requisição HTTP GET para uma URL:
requisicao = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(requisicao)

# Verificando o status da requisição
if requisicao.status_code == 200:
    data = requisicao.json()
    print("Requisição bem-sucedida!")
    print(f"Título da tarefa: {data['title']}")
else:
    print(f"Erro na requisição: {requisicao.status_code}")
