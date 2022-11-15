# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 04/11/2022
# Primeiro Programa em Python

# ImportaNndo a Biblioteca OS para usar o comando 'cls'
import os
 
# 'cls' usado para limpar toda a tela do terminal
os.system('cls')

# Declarações
nome = "Jhon Doe"
data_nascimento = 1970
altura = 1.77
peso = 72.5
doador = True
complexo = 3j
CONSTANTE = 10

# Saida
print("-"*70)
print("Estudo de Variáveis: TIPOS")
print("-"*70)
print("A variável nome é do tipo ", type(nome))
print("A variável data_nascimento é do tipo", type(data_nascimento))
print("A variável altura é do tipo", type(altura))
print("A variável peso é do tipo", type(peso))
print("A variável doador é do tipo", type(doador))
print("A variável complexo é do tipo", type(complexo))
print("A variável CONSTANTE é do tipo", type(CONSTANTE))

print("-"*70)

print()
print("-"*70)
print("Seu nome é....................: ", nome)
print("Ano de nascimento.............: ", data_nascimento)
print("Você mede.....................:", altura, "m")
print("Seu peso é....................:", peso, "Kg")
print("Impressão de número complexo..: ", complexo)
print("Impressão de uma costante", CONSTANTE)

print("-"*70)
print("Fim do Programa!")
print("-"*70)