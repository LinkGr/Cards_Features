# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 13/11/2022

# Operadores Logicos (AND, OR e NOT)

import os


os.system("cls")


# Declaração
condicao1 = True
condicao2 = False

# Teste de Condicional
if ((condicao1 == True and condicao2 == False) or
    (condicao1 != False and condicao2 != True)):
    # Se a Condição for verdadeira
    print("É verdadeiro")
else:
    # Se nenhuma condição for verdadeira
    print("É Falso")