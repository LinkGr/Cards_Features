# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 08/11/2022

# Atividade 3 Letra b)

import os


os.system("cls")


# Entrada
data_nascimento = int(input("Insira sua data de nascimento: "))
data_atual = int(input("Insira o ano atual: "))

# Calculos
idade = data_atual - data_nascimento

# Saida
print()
print("-"*30)
print("Calculo da Idade")
print("-"*30)
print(f"No ano {data_atual} sua idade é {idade}")
print("-"*30)