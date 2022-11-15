# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 14/11/2022

# Atividade 4 Letra g)

import os


os.system("cls")

# Declarações
lado_a = 0
lado_b = 0
lado_c = 0
comparacao = 0
resposta = ""

# Titulo
print("-"*30)
print("Formação de Triangulo")
print("-"*30)
print()

# Entrada
lado_a = float(input("Insira o lado A do triangulo: "))
lado_b = float(input("Insira o lado B do triangulo: "))
lado_c = float(input("Insira o lado C do triangulo: "))

# Condicional
# Nenhum lado pode ser 0 para possibilitar a conta
if ((lado_a != 0) and (lado_b != 0) and (lado_c != 0)):
    # Se o lado A for maior
    if ((lado_a > lado_b) and (lado_a > lado_c)):
        comparacao = lado_a < (lado_b + lado_c)
    # Se o lado B for maior
    elif ((lado_b > lado_a) and (lado_b > lado_c)):
        comparacao = lado_b < (lado_a + lado_c)
    # Se o lado C for maior
    else:
        comparacao = lado_c < (lado_a + lado_b)

    if(comparacao == True):
        resposta = f"Pode ser formado o triangulo com lados {lado_a}, {lado_b} e {lado_c}."
    else:
        resposta = f"O triangulo não pode ser formados com os lados {lado_a}, {lado_b} e {lado_c}."
else:
    resposta = "Nenhum dos lados pode ser igual a 0."

print()
print(resposta)
print()

print("-"*30)
print("Fim do Programa")
print("-"*30)