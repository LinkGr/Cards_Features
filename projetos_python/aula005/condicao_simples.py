# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 13/11/2022

# Condicional Simples

import os


os.system("cls")


# Titulo
print("-"*30)
print("Pratica: verificando valor quebrado")
print("-"*30)

# Entrada de Dados
valor = float(input("Digite um valor com casas decimais: "))

# Teste de Condicional
if (valor % 2 == 0 or valor == 1):
    # Se a Condição for verdadeira
    print(f"Valor {valor} invalido, o numero digitado é inteiro.")
else:
    # Se nenhuma condição for verdadeira
    print()
    print(f"O Valor digitado foi {valor}, entrada correta!")

print("-"*30)
print("Fim do Programa")
print("-"*30)