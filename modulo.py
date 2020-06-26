import math # inporta a biblioteca de matemática
num = float(input('Digite um número'))
while num<0:
    print('Ops! Não existe raíz quadrada de número negativo!')
    num = float(input('Favor informar um outro número.'))
raiz = math.sqrt(num) # minha variavel raiz recebe a raiz quadrada do numero recebido
print(f'A raiz quadrada de {num} é {raiz}')