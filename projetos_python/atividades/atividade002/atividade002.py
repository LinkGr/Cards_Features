# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 08/11/2022

# Calculos

import os


os.system("cls")


# Entrada
a = int(input("Insira o primeiro numero: "))
b = int(input("Insira o segundo numero: "))

# Calculos
# Soma
soma = a + b
# Subtracao
subtracao = a - b
# Produto
produto = a * b
# Divisão
divisao = a / b
# Potencia
potencia = a ** b
# Divisão Inteiro
divisao_inteiro = a // b
# Resto Divisão
resto_divisao = a % b
# Raiz Quadrada
raiz_quadrada = soma ** (1/2)
# Raiz Cubica
raiz_cubica = soma ** (1/3)

# Saida
print()
print("-"*70)
print("ESTUDO DE OPERADORES ARITMÉTICOS")
print("-"*70)
print(f"A soma de {a} + {b} = {soma}")
print(f"A subtração de {a} - {b} = {subtracao}")
print(f"A multiplicação de {a} * {b} = {produto}")
print(f"A divisão de {a} / {b} = {divisao:.2f}")
print(f"O numero {a} elevado a {b} = {potencia}")
print(f"A divisão inteira de {a} por {b} = {divisao_inteiro}")
print(f"O resto da divisão de {a} por {b} = {resto_divisao}")
print(f"A raiz quadrada de {a} é {raiz_quadrada:.2f}")
print(f"A raiz cubica de {a} é {raiz_cubica:.2f}")
print("-"*70)