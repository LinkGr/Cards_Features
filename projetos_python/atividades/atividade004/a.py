# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 14/11/2022

# Atividade 4 Letra a)

import os


os.system("cls")

# Titulo
print("-"*30)
print("Indentificar Par ou Impar")
print("-"*30)

# Entrada
numero = int(input("Escreva qualquer numero inteiro: "))
check = numero % 2

# Condicional
print()
if (check == 0):
    print("O numero é par!!")
else:
    print("O numero é impar!!")
print()

print("-"*30)
print("Fim do Programa")
print("-"*30)