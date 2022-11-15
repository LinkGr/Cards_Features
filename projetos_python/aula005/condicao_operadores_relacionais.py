# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 13/11/2022

# Condicional com Operadores Relacionais

import os


os.system("cls")

# Declaração
a = 10
b = 5
c = "José"
d = "José"

# Titulo
print("-"*30)
print("OPERADORES RELACIONAIS")
print("-"*30)

# Operador == igualdade 
if (c == d):
    print("-"*30)
    print(f"{c} é igual a {d}")
    print("-"*30)
else:
    print(f"{c} não é igual a {d}")
print()

# Operador != diferença
if (a != c):
    print("-"*30)
    print(f"{a} é diferente de {c}")
    print("-"*30)
else:
    print(f"{a} não é diferente de {c}")
print()

# Operador > maior que
if (a > b):
    print("-"*30)
    print(f"{a} é maior que {b}")
    print("-"*30)
else:
    print(f"{a} não é maior que {b}")
print()

# Operador < menor que
if (b < a):
    print("-"*30)
    print(f"{b} é menor que {a}")
    print("-"*30)
else:
    print(f"{b} não é menor que {a}")
print()

# Operador >= maior ou igual
if (a >= b):
    print("-"*30)
    print(f"{a} é maior ou igual a {b}")
    print("-"*30)
else:
    print(f"{a} não é maior ou igual a {b}")
print()

# Operador <= menor ou igual
if (b <= a):
    print("-"*30)
    print(f"{b} é menor ou igual a {a}")
    print("-"*30)
else:
    print(f"{b} não é menor ou igual a {a}")
print()

print("-"*30)
print("Fim do Programa")
print("-"*30)