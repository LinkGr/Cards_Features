# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 13/11/2022

# Condicional Operadores Logicos

import os


os.system("cls")

# Declaração
a = 10
b = 5
c = "Jhon"

print("-"*30)
print("Estudo de Condicional: Operadores Lógicos")
print("-"*30)
print()

# and (E) VERDADEIRO
print("and (E) VERDADEIRO")
if(a > 5 and b != c):
    print("Verdadeiro: Bloco Executado")
else:
    print("Falso: Block executado")

print()

# and (E) FALSO
print("and (E) FALSO")
if(a > 5 and b == c):
    print("Verdadeiro: Bloco Executado")
else:
    print("Falso: Block executado")

print()

# or (OU) VERDADEIRO
print("or (OU) VERDADEIRO")
if(a > 5 or b == c):
    print("Verdadeiro: Bloco Executado")
else:
    print("Falso: Block executado")

print()

# or (OU) FALSO
print("or (OU) FALSO")
if(a < 5 or c == "Jane"):
    print("Verdadeiro: Bloco Executado")
else:
    print("Falso: Block executado")