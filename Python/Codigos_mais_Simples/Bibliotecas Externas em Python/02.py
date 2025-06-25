import requests 

def obter_fato_gato():
    url = "https://catfact.ninja/fact"

    try:
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            
            return dados['fact']
        else:
            return f"Erro ao buscar fato: Status {resposta.status_code}"
    except requests.exceptions.ConnectionError:
        return "Erro de conexão: Verifique sua internet."
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"

if __name__ == "__main__":
    print("Buscando um fato aleatório sobre gatos...")
    fato = obter_fato_gato()
    print("\nFato de Gato:")
    print(fato)