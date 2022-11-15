# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 14/11/2022

# Atividade 4 Letra d)

import os


os.system("cls")

# Declarações
salario = 0
porcentagem = 0.00
aumento = 0
salario_aumentado = 0
resposta = ""

# Titulo
print("-"*30)
print("Calculo de aumento salarial")
print("-"*30)
print()

# Entrada
salario = float(input("Insira o salario: "))

# Condicional
if (salario > 0):
    if (salario <= 1000):
        porcentagem = 10
        aumento = salario * 0.10
        salario_aumentado = salario + aumento
        resposta = f"O salario foi aumentado em {porcentagem}% e passou a ser {salario_aumentado}"
    elif (salario >= 1500):
        porcentagem = 5
        aumento = salario * 0.05
        salario_aumentado = salario + aumento
        resposta = f"O salario foi aumentado em {porcentagem}% e passou a ser {salario_aumentado}"
    else:
        pass
else:
    resposta = "Resposta invalida - O salario não pode ser negativa ou zero"

print()
print(resposta)
print()

print("-"*30)
print("Fim do Programa")
print("-"*30)