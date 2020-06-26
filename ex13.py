print('Escolha uma das opções a seguir:')
print('1. Inposto')
print('2. Novo Salário')
print('3. Classificação')
opcao = input('')
if opcao>0 and opcao<=3:
    salario = float(input('Informe seu salário'))
    if opcao ==1:
        
            if salario <500:
                imposto = salario*(0.05)
                print('O imposto sobre seu salário é de R$',imposto)
            elif salario>=500 and salario<=850:
                imposto = salario*(0.1)
                print('O imposto sobre seu salário é de R$',imposto)
            elif salario>850:
                imposto = salario*(0.15)
                print('O imposto sobre seu salário é de R$',imposto)
    if opcao ==2:
        if salario


else:
    print('Opção inválida.')