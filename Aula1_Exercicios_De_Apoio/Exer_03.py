N1 = float(input("Digite a 1ª Nota: "))
N2 = float(input("Digite a 2ª Nota: "))
N3 = float(input("Digite a 3ª Nota: "))

soma = 0

soma = (N1 + N2 + N3) / 3

soma_arredondada = round(soma, 2)  # Arredonda para 2 casas decimais antes da comparação

if soma_arredondada >= 5:
    print(f"Aluno aprovado com nota = {soma_arredondada:.2f}")
else:
    print(f"Aluno reprovado com nota = {soma_arredondada:.2f}")