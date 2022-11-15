# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 14/11/2022

# Atividade 4 Letra h)

import os


os.system("cls")

# Declarações
a = 0
b = 0
c = 0
delta = 0
x1 = 0
x2 = 0
resposta = ""

# Titulo
print("-"*30)
print("- Equação de segundo grau")
print("-"*30)
print()

# Entrada
a = float(input("Insira a variavel 'a' da equação: "))
b = float(input("Insira a variavel 'b' da equação: "))
c = float(input("Insira a variavel 'c' da equação: "))

# Regras para a equação do segundo grau ser possivel:
# a != 0
# a, b e c tem que pertencer aos numeros reais

# Condicional
# Se a != 0
if (a != 0):
    delta = (b ** 2) - (4 * a * c)
    
    if (delta >= 0):
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)

        resposta = f"A equação apresenta duas raizes possiveis: {x1} e {x2}"
    else:
        resposta = "A equação não possui solução dentro do conjunto dos numeros reais"
else:
    resposta = "A equação não pode ser considerada como de segundo grau pois 'a' tem que ser diferente de 0"

print()
print(resposta)
print()

print("-"*30)
print("Fim do Programa")
print("-"*30)