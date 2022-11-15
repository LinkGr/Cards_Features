# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 08/11/2022

# Atividade 3 Letra i)

import os


os.system("cls")


# Entrada
valor = float(input("Insira o valor desejado: R$"))

# Calculos
DOLAR = float(5.19)
valor_convertido = valor / DOLAR

# Saida
print()
print("-"*30)
print(f"Conversor de Dolar pra Real - (Dolar Atual em {DOLAR:.2f})")
print("-"*30)
print(f"Valor em Reais: {valor:.2f}")
print(f"Valor em dolar: {valor_convertido:.2f}")
print("-"*30)