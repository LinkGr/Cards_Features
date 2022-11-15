# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 14/11/2022

# Atividade 4 Letra b)

import os


os.system("cls")

# Declarações
numero1 = 0
numero2 = 0
numero3 = 0
maior = ""
menor = ""

# Titulo
print("-"*30)
print("Maior e Menor")
print("-"*30)
print()

# Entrada
numero1 = int(input("Escreva o primeiro numero: "))
numero2 = int(input("Escreva o segundo numero: "))
numero3 = int(input("Escreva o terceiro numero: "))

# Condicional
print()
# Se os numeros forem diferentes
if ((numero1 != numero2) or (numero2 != numero3)):
    # Checando o maior numero
    if ((numero1 > numero2) and (numero1 > numero3)):
        maior = f"O numero {numero1} é o maior!!"
    elif ((numero2 > numero1) and (numero2 > numero3)):
        maior = f"O Numero {numero2} é o maior!"
    else:
        maior = f"O Numero {numero3} é o maior!"

# Checando o menor numero
    if ((numero1 < numero2) and (numero1 < numero3)):
        menor = f"O numero {numero1} é o menor!"
    elif ((numero2 < numero1) and (numero2 < numero3)):
        menor = f"O Numero {numero2} é o menor!"
    else:
        menor = f"O Numero {numero3} é o menor!"
    # Saida
    print(maior)
    print(menor)

# Se eles não forem diferentes
else:
    print(f"Os 3 numeros apresentados são iguais!!")

print()
print("-"*30)
print("Fim do Programa")
print("-"*30)