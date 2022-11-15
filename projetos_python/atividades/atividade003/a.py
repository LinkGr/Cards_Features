# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 08/11/2022

# Atividade 3 Letra a)

import os


os.system("cls")


# Entrada
a = int(input("Insira o primeiro numero: "))
b = int(input("Insira o segundo numero: "))
c = int(input("Insira o terceiro numero: "))

# Calculos
# Soma
soma = a + b + c
# Produto
produto = a * b * c

# Saida
print()
print("-"*70)
print("Soma e Multiplicação")
print("-"*70)
print(f"A soma de {a} + {b} + {c} = {soma}")
print(f"A multiplicação de {a} * {b} * {c} = {produto}")
print("-"*70)