# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 07/11/2022

# Atividade 001

import os


os.system("cls")


# -Entrada-
# Pessoal:
nome = str(input("Nome completo: "))
nascimento = int(input("Data de Nascimento: "))
rg = int(input("RG (Somente numeros): "))
cpf = int(input("CPF (Somente numeros): "))
# Endereço:
rua = str(input("Rua: "))
numero = str(input("Número: "))
complemento = input("Complemento: ")
cep = int(input("CEP (Somente numeros): "))
cidade = str(input("Cidade: "))
estado = str(input("Estado: "))
pais = str(input("País: "))


# -Saida-

print()
print("--------------------------------Formulario de dados--------------------------------")
print("|Pessoal:")
print(f"|    Nome completo: {nome}")
print(f"|    Nascimento: {nascimento}")
print(f"|    CPF: {cpf}")
print(f"|    RG: {rg}")
print("|")
print("|Endereço:")
print(f"|    Rua: {rua}")
print(f"|    Numero: {numero}")
print(f"|    CEP: {cep}")
print(f"|    Complemento: {complemento}")
print(f"|    Cidade: {cidade}")
print(f"|    Estado: {estado}")
print(f"|    País: {pais}")
print("-----------------------------------------------------------------------------------")
print()