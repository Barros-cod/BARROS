import datetime
import os

# Definindo o nome do arquivo de lista de compras
caminho_arquivo = "Python/01/lista_compras.txt"

def adicionar_item():
    """ Adiciona uma nova entrada na lista de compras com seu data e hora! """
    try:
        with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
            adicionar_item_lista = input("Digite o nome do item a ser adicionado: ")
            if adicionar_item_lista.lower() == '0':
                return True
            
            data_hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivo.write(f"[{data_hora_atual}] Item '[{adicionar_item_lista}]' adicionado à lista.\n")
            return True
    except Exception as e:
        print(f"Erro ao adicionar item: {e}")
        return True
        
def visualizar_lista():
    """ Visualiza os itens detro da lista """
    try:
        if not os.path.exists(caminho_arquivo):
            print("Lista de Compras não existe.")
            return
        
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if not conteudo.strip():
                print("Lista esta Vazia, adicione uma entrada primero!")
            else:
                print("--- Sua Lista de Compras ---")
                print(conteudo)
    except FileNotFoundError: 
        print("Erro: O arquivo do diário não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o diário: {e}")

def remover_item():
    """ Remove um item da lista de compras """
    try:
        if not os.path.exists(caminho_arquivo):
            print("Lista de compras não existe.")
            return

        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("Lista está vazia.")
            return

        print("\nItens na lista:")
        for idx, linha in enumerate(linhas, start=1):
            print(f"{idx}. {linha.strip()}")

        escolha = input("\nDigite o número do item que deseja remover (ou 0 para cancelar): ").strip()
        if escolha == '0':
            return

        index = int(escolha) - 1
        if 0 <= index < len(linhas):
            item_removido = linhas.pop(index)
            with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
                arquivo.writelines(linhas)
            print(f"Item removido: {item_removido.strip()}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
    except Exception as e:
        print(f"Erro ao remover item: {e}")



print("\n==== Bem-vindo Lista de Compras! ====")

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar item ")
    print("2. Visualizar lista ")
    print("3. Remover item")
    print("0. Sair do programa")

    escolha = input("Sua escolha: ").strip() 

    if escolha == "1":
        if not adicionar_item():
            break
    elif escolha == "2":
        visualizar_lista()
    elif escolha == "3":
        remover_item()
    elif escolha == "0":
        print("\nProgram finalizado!")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2, 3 ou 0.")