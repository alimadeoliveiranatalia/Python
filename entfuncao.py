# Função com entrada de parâmetros sem retorno
def Ola(meu_nome):
    print(f'Olá {meu_nome}, bem vinda, que bom que estais programando em Python!')
# Função com entrada de parâmetros com retorno
def calcular_pagamento(salario):
    aumento = salario*0.5
    novo_salario = salario+aumento
    return novo_salario
# Programa Principal:
meu_nome=input('Informe seu nome, por favor. ' ) # entrada de parâmetros
Ola(meu_nome) # chamada da função
salario = float(input('Informe seu salário, por gentileza: ' ))
salario_ajustado = calcular_pagamento(salario) 
print(f'Seu salário ajustado é: R${salario_ajustado}') 