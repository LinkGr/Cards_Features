# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 08/11/2022

# Atividade 3 Letra c)

import os


os.system("cls")


# Entrada
nota1 = float(input("1º Nota: "))
nota2 = float(input("2º Nota: "))
nota3 = float(input("3º Nota: "))
nota4 = float(input("4º Nota: "))

# Operações
soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

# Saida
print()
print("-"*30)
print("Calculo da Média")
print("-"*30)
print(f"A média das quatro notas é: {media:.1f}")
print("-"*30)