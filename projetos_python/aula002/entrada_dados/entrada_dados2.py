# Curso Técnico de Informática
# Autor: Juanito a Maquina
# Data: 07/11/2022

# Uso do comando input 2

import os


os.system("cls")


# Entrada
nome = str(input("Nome completo: "))
endereco = str(input("Digite o endereço: "))
cep = int(input("Entre com o cep (Sem traço nem ponto): "))
cidade = str(input("Digite o nome da cidade: "))
estado = str(input("Entre com o estado: "))
nota_enem = float(input("Digite sua nota no Enem: "))


# Saida

print()
print("-"*70)
print("ESTUDO DE ENTRADA DE DADOS COM INPUT 2")
print("-"*70)
# Dentro desse print usamos o f (ou format) que permite o uso de variaveis junto das aspas com elas entre chaves  
print(f"Nome completo: {nome}")
print(f"Endereço: {endereco}")
print(f"CEP: {cep}")
print(f"Cidade: {cidade}")
print(f"Estado: {estado}")
print(f"Nota no Enem: {nota_enem:.2f}")
print("-"*70)
print("Fim do Programa!!")
print("-"*70)
print()