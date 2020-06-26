# Programa que calcula o salario atual de um funcionário:
# a) O funcionário foi contratado em 2005, com salário inicial de R$1000,00.
# b) Em 2006, ele recebeu aumento de 1,5% sobre seu salário.
# c) A partir de 2007(inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
ano_atual=int(input('Informe o ano em exercicio: ' ))
salario_inicial = 1000.00
percentual_inicial = 0.015
salario_em_2006 = salario_inicial+percentual_inicial*salario_inicial
print(f'Seu salário em 2006 era de R${salario_em_2006},00') 
salario_ajustado=salario_em_2006
for i in range (2006,ano_atual):
    percentual_inicial=2*percentual_inicial
    salario_ajustado=salario_ajustado+percentual_inicial*salario_ajustado
print(f'Seu salário ajustado agora é de: R${salario_ajustado},00')                                                              