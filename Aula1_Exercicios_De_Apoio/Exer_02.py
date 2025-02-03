# Define uma lista de palavras
palavra = ['taco', 'bola', 'celeiro', 'cesta', 'peteca', 'zebra', 'ama', 'zon']

# Inicializa variáveis para armazenar a primeira e a última palavras em ordem alfabética
primeira = ""
ultima = ""

# Encontra a primeira palavra em ordem alfabética
primeira = min(palavra)

# Encontra a última palavra em ordem alfabética
ultima = max(palavra)

# Imprime a primeira palavra em ordem alfabética
print("Primeira palavra em ordem alfabética é: ", primeira)

# Imprime a última palavra em ordem alfabética
print("Ultima palavra em ordem alfabética é: ", ultima)

# Imprime a concatenação da primeira e última palavras
print(primeira+ultima)

