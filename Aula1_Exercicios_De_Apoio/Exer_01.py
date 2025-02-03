"""
Este script converte uma temperatura de Celsius para Fahrenheit.

O usuário é solicitado a inserir uma temperatura em Celsius, que é então convertida
para Fahrenheit usando a fórmula: F = (C * 9 / 5) + 32. O resultado é impresso no console.
"""

# Solicita ao usuário para inserir uma temperatura em Celsius
C = float(input("Digite a temperatura em ºC: "))

# Converte a temperatura para Fahrenheit
F = (C * 9 / 5) + 32

# Imprime a temperatura em Fahrenheit
print("A temperatura em Fahrenheit é: ", F)