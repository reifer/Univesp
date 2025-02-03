"""
Este script calcula a média de três notas e determina se o aluno está aprovado ou não.

O usuário é solicitado a inserir três notas. O script então calcula a média dessas notas,
arredonda para duas casas decimais e imprime se o aluno está aprovado (média >= 5) ou não.
"""

# Solicita ao usuário para inserir a primeira nota
N1 = float(input("Digite a 1ª Nota: "))

# Solicita ao usuário para inserir a segunda nota
N2 = float(input("Digite a 2ª Nota: "))

# Solicita ao usuário para inserir a terceira nota
N3 = float(input("Digite a 3ª Nota: "))

# Inicializa a variável para armazenar a soma das notas
soma = 0

# Calcula a média das três notas
soma = (N1 + N2 + N3) / 3

# Arredonda a média para 2 casas decimais antes da comparação
soma_arredondada = round(soma, 2)

# Verifica se a média arredondada é maior ou igual a 5
if soma_arredondada >= 5:
    # Imprime que o aluno está aprovado com a média arredondada
    print(f"Aluno aprovado com nota = {soma_arredondada:.2f}")
else:
    # Imprime que o aluno está reprovado com a média arredondada
    print(f"Aluno reprovado com nota = {soma_arredondada:.2f}")