# Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:
#
# a) A soma de 2 e 2 é menor que 4.
a = 2 + 2 < 4
print(a)

# b) O valor de 7 // 3 é igual a 1 + 1.
b = 7 // 3 == 1 + 1
print(b)

# c) A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
c = 3 ** 2 + 4 ** 2 == 25
print(c)

# d) A soma de 2, 4 e 6 é maior que 12.
d = 2 + 4 + 6 > 12
print(d)

# e) 1387 é divisível por 19.
e = 1387 % 19 == 0
print(e)

# f) 31 é par. (Dica: o que o resto lhe diz quando vocêdivide por 2?)
f = 31 % 2 == 0
print(f)

# g) O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*
g = min(34.99, 29.95, 31.50) < 30.00
print(g)