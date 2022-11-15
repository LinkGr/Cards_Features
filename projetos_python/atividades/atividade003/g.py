# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 08/11/2022

# Atividade 3 Letra g)

import os


os.system("cls")


# Entrada
metros = float(input("Insira a medida em metros: "))

# Calculos
centimetros = metros * 100
milimetros = centimetros * 10


# Saida
print()
print("-"*30)
print("---Conversor de medidas---")
print(f"{metros}m")
print(f"Em centimetros: {centimetros}cm")
print(f"Em milimetros: {milimetros}mm")
print("-"*30)