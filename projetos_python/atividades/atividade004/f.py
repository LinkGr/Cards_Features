# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 14/11/2022

# Atividade 4 Letra f)

import os


os.system("cls")

# Declarações
ano = 0
resposta = ""

# Titulo
print("-"*30)
print("Calculo de aumento salarial")
print("-"*30)
print()

# Entrada
ano = float(input("Digite um ano aleatorio: "))

# Condicional
if (ano > 0):
    # Se o ano for divisivel por 4 ou 400 e não foi divisivel por 100
    if (((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0)):
        resposta = f"O ano {ano} é bissexto!!"
    else:
        resposta = f"O ano {ano} não é bissexto!!"
else:
    resposta = "Resposta invalida!!"

print()
print(resposta)
print()

print("-"*30)
print("Fim do Programa")
print("-"*30)