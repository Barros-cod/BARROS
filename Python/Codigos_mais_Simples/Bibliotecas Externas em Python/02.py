# import requests 

# try:
#     response = requests.get('https://www.google.com')
    
#     response.raise_for_status()
#     print(f"Status Code da Google: {response.status_code}")
#     print(f"Conteúdo parcial da Google: {response.text[:200]}...")
# except requests.exceptions.RequestException as e:
#     print(f"Ocorreu um erro: {e}")

# print("-" * 30)

# params = {'nome': 'Fulano', 'idade': 30}
# try:
#     response = requests.get("https://httpbin.org/get", params=params)
#     response.raise_for_status()
#     print(f"Status Code com parâmetros: {response.status_code}")
#     print(f"JSON retornado com parâmetros: {response.json()}")
# except requests.exceptions.RequestException as e:
#     print(f"Ocorreu um erro: {e}")

# input("")

# def obter_fato_gato():
#     url = "https://catfact.ninja/fact"

#     try:
#         resposta = requests.get(url)

#         if resposta.status_code == 200:
#             dados = resposta.json()
            
#             return dados['fact']
#         else:
#             return f"Erro ao buscar fato: Status {resposta.status_code}"
#     except requests.exceptions.ConnectionError:
#         return "Erro de conexão: Verifique sua internet."
#     except Exception as e:
#         return f"Ocorreu um erro inesperado: {e}"

# if __name__ == "__main__":
#     print("Buscando um fato aleatório sobre gatos...")
#     fato = obter_fato_gato()
#     print("\nFato de Gato:")
#     print(fato)