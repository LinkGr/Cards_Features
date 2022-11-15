# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 14/11/2022

# Atividade 4 Letra c)

import os


os.system("cls")

# Declarações
velocidade = 0
resposta = ""

# Titulo
print("-"*30)
print("Aviso de Velocidade")
print("-"*30)
print()

# Entrada
velocidade = int(input("Escreva o primeiro numero (km/h): "))

# Condicional
if (velocidade > 0):
    if(velocidade <= 60):
        resposta = f"A velocidade de {velocidade}km/hr é permitida!" 
    else:
        resposta = f"AVISO: A velocidade de {velocidade}km/hr é acima do permitido!" 
else:
    resposta = "Velocidade invalida - A velocidade não pode ser negativa ou zero"

print()
print(resposta)
print()

print("-"*30)
print("Fim do Programa")
print("-"*30)