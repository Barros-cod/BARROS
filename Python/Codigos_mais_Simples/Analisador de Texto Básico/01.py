
# Analisador de Texto Básico!
# Você vai criar um programa que analisa um pequeno texto e nos dá algumas informações sobre ele.

# Tarefa:

# Crie um Dicionário para Contar Palavras:

# Crie uma função chamada contar_palavras(texto) que recebe uma string de texto como argumento.
# Dentro dessa função, crie um dicionário vazio.
# O objetivo é contar a frequência de cada palavra no texto:
# Percorra as palavras do texto (dica: use .split() para dividir o texto em palavras).
# Para cada palavra, use-a como chave no dicionário.
# O valor associado à chave será a quantidade de vezes que a palavra aparece.
# Se a palavra já estiver no dicionário, incremente seu contador. Se não, adicione-a com o contador 1.
# Importante: Converta as palavras para minúsculas (.lower()) para que "Python" e "python" sejam contadas como a mesma palavra.
# Exemplo de como o dicionário ficaria:
# {"python": 2, "é": 1, "legal": 1}

# Crie um Conjunto para Palavras Únicas:

# Crie uma função chamada encontrar_palavras_unicas(texto) que recebe uma string de texto.
# Dentro dela, crie um conjunto vazio.
# Percorra as palavras do texto (lembre-se de converter para minúsculas!).
# Adicione cada palavra ao conjunto.
# Retorne o conjunto de palavras únicas.
# Simule a Interação:

# Defina uma string de texto de exemplo (pode ser uma frase simples e repetitiva para testar, por exemplo: "Python é legal. Python é poderoso.").
# Chame a função contar_palavras() com seu texto e imprima o dicionário resultante.
# Chame a função encontrar_palavras_unicas() com seu texto e imprima o conjunto resultante.
# Dicas:

# Lembre-se que minha_string.split() sem argumentos divide a string por espaços em branco e lida com múltiplos espaços.
# Para verificar se uma chave já existe em um dicionário antes de incrementar, você pode usar if palavra in meu_dicionario: ou o método meu_dicionario.get(palavra, 0) para obter o valor atual ou 0 se a chave não existir.
