# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 07/11/2022

# Uso do comando input

import os


os.system("cls")


# Entrada
nome = str(input("Qual o seu nome: "))
data_nascimento = int(input("Em que ano você nasceu: "))
altura = float(input("Qual a sua altura: "))
peso = float(input("Quanto você pesa: "))


# Saida

print()
print("-"*70)
print("ESTUDO DE ENTRADA DE DADOS COM INPUT")
print("-"*70)
# Dentro desse print usamos o f (ou format) que permite o uso de variaveis junto das aspas com elas entre chaves  
print(f"Seu nome é................: {nome}")
print(f"Ano de nascimento.........: {data_nascimento}")
print(f"Você mede.................: {altura} m")
print(f"Seu peso é................: {peso} Kg")
print("-"*70)
print("Fim do Programa!!")
print("-"*70)
print()