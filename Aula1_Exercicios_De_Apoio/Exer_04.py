"""
Este script calcula a soma dos números de 1 a 100.

O script utiliza um loop `for` para iterar pelos números de 1 a 100 (inclusive),
somando cada número a uma variável acumuladora. O resultado é então impresso no console.
"""

# Inicializa a variável para armazenar a soma dos números
soma = 0

# Loop através dos números de 1 a 100 (inclusive)
for i in range(1, 101):
    # Adiciona o número atual à soma
    soma += i

# Imprime a soma dos primeiros 100 números
print("A soma dos 100 primeiros números é: ", soma)