# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 13/11/2022

# Condicional Simples e Aninhada

import os


os.system("cls")

# Declaração
a = 10
b = 5
c = "Jhon"


# Condicional Simples
print("-"*30)
print("Condicional Simples")
print("-"*30)
if (a > b):
    # Se a Condição for verdadeira
    print('"a" é maior que "b"!')
else:
    # Se nenhuma condição for verdadeira
    print()
    print('"a" não é maior que "b"')
print()

# Condicional Aninhada
print("-"*30)
print("Condicional Aninhada")
print("-"*30)
if (a < b):
    # Se a Condição for verdadeira
    print('"a" é menor que "b"!')
elif (b != 5):
    # Se a Condição anterior for falsa e essa nova for verdadeira
    print('"b" é diferente de "c"!')
elif (c == "Jhon"):
    # Se a Condição anterior for falsa e essa nova for verdadeira
    print('"c" é igual a "Jhon"')
else:
    # Se nenhuma condição for verdadeira
    print()
    print('Nenhuma condição era verdadeira')
print()

print("-"*30)
print("Fim do Programa")
print("-"*30)