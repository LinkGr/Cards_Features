# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 14/11/2022

# Atividade 4 Letra e)

import os


os.system("cls")

# Declarações
distancia = 0
preco_por_kilometro = 0
preco_passagem = 0
resposta = ""

# Titulo
print("-"*30)
print("Calculo de aumento salarial")
print("-"*30)
print()

distancia = float(input("Insira a distancia da viagem: "))

# Condicional
if (distancia > 0):
    if (distancia <= 200):
        preco_por_kilometro = 0.70
    elif (distancia > 200):
        preco_por_kilometro = 0.40
    else:
        pass
else:
    resposta = "Resposta invalida - A distancia não pode ser negativa ou zero"

preco_passagem = distancia * preco_por_kilometro
resposta = f"O preço de uma viagem de distancia {distancia}Km é R${preco_passagem:.2f}!!"

print()
print(resposta)
print()

print("-"*30)
print("Fim do Programa")
print("-"*30)