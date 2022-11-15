# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 07/11/2022

# Calculos

import os


os.system("cls")


# Entrada
nota1 = float(input("1º Nota: "))
nota2 = float(input("2º Nota: "))
nota3 = float(input("3º Nota: "))
nota4 = float(input("4º Nota: "))

# Operações
soma = nota1 + nota2 + nota3 + nota4
media = nota1 + nota2 + nota3 + nota4 / 4
media_certa = (nota1 + nota2 + nota3 + nota4) / 4

# Saida
print()
print("-"*70)
print(f"1º nota do aluno: {nota1}")
print(f"2º nota do aluno: {nota2}")
print(f"3º nota do aluno: {nota3}")
print(f"4º nota do aluno: {nota4}")
print(f"A soma das notas é: {soma}")
print(f"A média: {media:.1f} ERRADO!")
print(f"A média: {media_certa:.1f} CORRETO!")
print("-"*70)