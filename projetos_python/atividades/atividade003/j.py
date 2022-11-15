# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 08/11/2022

# Atividade 3 Letra j)

import os


os.system("cls")


# Entrada
base = int(input("Insira a base do retangulo (cm): "))
altura = int(input("Insira a altura do retangulo (cm): "))

# Calculos
perimetro = base * 2 + altura * 2

# Saida
print()
print("-"*30)
print("Calculo de Perimetro: ")
print("-"*30)
print(f"O perimetro do retangulo com base {base} e altura {altura} é")
print(f"{base} + {base} + {altura} + {altura} = {perimetro}")
print("-"*30)