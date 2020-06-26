def menu():
    print('1. Imposto')
    print('2. Novo Salário')
    print('3. Classificação')
def calcular_imposto():
    salario=float(input('Informe seu salário, por gentileza!'))
    if salario<500:
        imposto=salario*0.05
        print(f'O imposto é de: R${imposto}')
    elif salario>=500 and salario<850:
        imposto=salario*0.1
        print(f'O imposto é de: R${imposto}')
    elif salario>=850:
        imposto=salario*0.15
        print(f'O imposto é de: R${imposto}')
def calcular_novo_salario():
    salario=float(input('Informe seu salário, por gentileza!'))
    if salario>1500:
        salario_com_aumento=salario+25
        print(f'Seu novo salário é de: R${salario_com_aumento}')
    elif salario>=750 and salario<=1500:
        salario_com_aumento=salario+50
        print(f'Seu novo salário é de: R${salario_com_aumento} ')
    elif salario>=450 and salario<750:
        salario_com_aumento=salario+75
        print(f'Seu novo salário é de: R${salario_com_aumento}')
    elif salario<450:
        salario_com_aumento=salario+100
        print(f'Seu novo salário é de: R${salario_com_aumento}')
def classificar():
    salario=float(input('Informe seu salário, por gentileza!'))
    if salario<=750:
        print('Você está sendo mal remunerado!')
    else:
        print('Você é bem remunerado! Parabêns!')
# Programa Principal:
menu() # Função que mostra as alternativas
opcao=int(input('Escolha uma das opções acima:'))
while opcao!=1 and opcao!=2 and opcao!=3: # Condição para travar o usuário de tal forma que ele escolha as opções propostas
    print('Não existe ação para a opção informada, por favor, escolha apenas uma das opções abaixo:')
    menu()
    opcao=int(input('Escolha uma das opções acima:'))
if opcao==1: # Se ele escolher a opção 1: chame a função que calcula o imposto
    calcular_imposto()
elif opcao==2: # Se ele escolher a opção 2: chame a função que calcula o novo salário
    calcular_novo_salario()
elif opcao==3: # Se ele escolher a opção 3: chame a função que mostra a classificação
    classificar()