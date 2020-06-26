codigo = int(input('Informe o código, por favor'))

if codigo == 1:
    salario = float(input('Informe o salário, por favor'))
    print('Escrituário')
    aumento = salario*(0.5)
    novo_salario = salario+aumento
    print('O Aumento foi de R$',aumento)
    print('Seu salário ajustado é de R$',novo_salario)
if codigo == 2:
    salario = float(input('Informe o salário, por favor'))
    print('Secretária')
    aumento = salario*(0.35)
    novo_salario = salario+aumento
    print('O aumento foi de R$',aumento)
    print('Seu salário ajustado é de R$',novo_salario)
if codigo ==3:
    salario = float(input('Informe o salário, por favor'))
    print('Caixa')
    aumento = salario*(0.2)
    novo_salario = salario+aumento
    print('O aumento foi de  R$', aumento)
    print('Seu salário ajustado é de R$',novo_salario)
if codigo == 4:
    salario = float(input('Informe o salário, por favor'))
    print('Gerente')
    aumento = salario*(0.1)
    novo_salario = salario+aumento
    print('O aumento foi de R$', aumento)
    print('Seu salário ajustado é de R$',novo_salario)
if codigo == 5:
    print('Diretor')
    print('Infelizmente veu salário não pode ser ajustado. Lamento.')