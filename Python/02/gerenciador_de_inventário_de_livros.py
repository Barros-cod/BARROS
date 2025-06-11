#Gerenciador de Inventário de Livros
# Listar os livros iniciais.
# Listar os gêneros únicos iniciais.
# Adicionar um livro novo.
# Adicionar um livro que já existe (para testar a atualização de quantidade).
# Vender um livro (quantidade suficiente).
# Vender um livro (quantidade insuficiente).
# Listar os livros novamente para ver as mudanças.
# Listar os gêneros únicos novamente.
inventario_livros = {
    "O Hobbit": {"autor": "J.R.R. Tolkien", "ano_publicacao": 1937, "genero": "Fantasia", "quantidade": 0},
    "1984": {"autor": "George Orwell", "ano_publicacao": 1949, "genero": "Distopia", "quantidade": 3},
    "The Art of Exploitation": {"autor": "Jon Erickson", "ano_publicacao": 2007, "genero": "Hacking", "quantidade": 4}
}

def livros_disponivel():
    if not inventario_livros:
        print("Nenhum livro no inventário.")
        return
    for titulo, detalhes in inventario_livros.items():
        print(f"\nTítulo: {titulo}")
        print(f"  Autor: {detalhes['autor']}")
        print(f"  Ano de Publicação: {detalhes['ano_publicacao']}")
        print(f"  Gênero: {detalhes['genero']}")
        print(f"  Quantidade: {detalhes['quantidade']}")

#Adicionar um livro novo.
def adicionar_livro():
    titulo_novo = input("Digite o título do livro: ")
    autor_novo = input(f"Digite o autor de '{titulo_novo}': ")
    ano_publicacao_novo = int(input(f"Digite o ano de publicação de '{titulo_novo}': "))
    genero_novo = input(f"Digite o gênero de '{titulo_novo}': ")
    quantidade_nova = int(input(f"Digite a quantidade de cópias de '{titulo_novo}': "))
    
    inventario_livros[titulo_novo] = {
        "autor": autor_novo,
        "ano_publicacao": ano_publicacao_novo,
        "genero": genero_novo,
        "quantidade": quantidade_nova
    }
    print(f"Livro '{titulo_novo}' adicionado com sucesso!")

def vender_livro():
    for titulo in inventario_livros.items():
        print(f"\nTítulo: {titulo}")

    nome_livro = input("Digite um nome do livros disponivel: ")
    
    if nome_livro in inventario_livros:
        print(f"  Quantidade: {inventario_livros['quantidade']}")




print("\n--- Gerenciador de Inventário de Livros: ---")

while True:
    print("\nEscolha uma opção:")
    print("1. Listar os livros iniciais.")
    print("2. Adicionar um livro novo.")
    print("3. Vender um livro.")
    print("4. Remover um livro.")
    print("0. Sair do programa")

    escolha = input("\nSua escolha: ").strip()

    if escolha == "1":
        print("\n=== Livros disponiveis ===\n")
        livros_disponivel()
    elif escolha == "2":
        adicionar_livro()
    elif escolha == "3":
        vender_livro()
    elif escolha == "4":
        ...
    elif escolha == "0":
        print("\nProgram finalizado!")
        break
    else:
        print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 0.")
           
