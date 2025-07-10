import requests

# Objetivo:
# Fazer uma requisição GET para listar tarefas filtradas por um critério (ID do usuário).
# Fazer uma requisição POST para criar uma nova tarefa.

def listar_tarefas_por_usuario(user_id):
    url = "https://jsonplaceholder.typicode.com/todos"
    try:
        response = requests.get(url, params={'userId': user_id})
        if response.status_code == 200: # 
            tarefas = response.json()
            if tarefas:
                print(f"\nTarefas do usuário {user_id}:\n")
                for tarefa in tarefas:
                    print(f"ID: {tarefa['id']}, Título: {tarefa['title']}, Concluída: {tarefa['completed']}")
            else:
                print(f"\nNenhuma tarefa encontrada para o usuário {user_id}.")
        else:
            print(f"\nErro ao buscar tarefas. Código de status: {response.status_code}")
    except requests.ConnectionError:
        print("\nErro de conexão. Verifique sua internet e tente novamente.")

def criar_nova_tarefa(user_id, titulo):
    url = "https://jsonplaceholder.typicode.com/todos"
    novo_tarefa = {
        'userId': user_id,
        'title': titulo,
        'completed': False
    }
    try:
        response = requests.post(url, json=novo_tarefa)
        if response.status_code in [200, 2001]:
            resultado = response.json()
            print(f'Tarefa criada com sucesso! ID: {resultado['id']}')
        else:
            print(f"\nErro ao criar tarefa. Código de status: {response.status_code}")
    except requests.ConnectionError:
        print("\nErro de conexão. Verifique sua internet e tente novamente.")

def menu_interativo():
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Listar tarefas por usuário")
        print("2. Criar nova tarefa")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")
    
        if escolha == '1':
            try:
                user_id = int(input("Digite o ID do usuário: "))
                listar_tarefas_por_usuario(user_id)
            except ValueError:
                print("ID inválido. Por favor, insira um número inteiro.")
        elif escolha == '2':
                try:
                    user_id = int(input("Digite o ID do usuário: "))
                    titulo = input("Digite o título da tarefa: ")
                    if titulo.strip() == "":
                        print("O título não pode ser vazio.")
                    else:
                        criar_nova_tarefa(user_id, titulo)
                except ValueError:
                    print("ID inválido. Por favor, insira um número inteiro.")
        elif escolha == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == '__main__':
    menu_interativo()