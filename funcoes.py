# Função com passagem de parâmetros e com retorno
def somar(a,b): # recebem valores no momento em que são chamadas
    a = int(a)
    b = int(b)
    soma = a+b
    return soma # devolvem um valor para quem as chamou 
# Função sem passagem de parâmetros e com retorno
def subtrair(): # Não recebem valores no momento em que são chamadas 
    a = int(x)
    b = int(y)
    sub = a-b
    return sub # retornam um valor para quem as chamou
# Função com passagem de parâmetros e sem retorno
def multiplicar(a,b): # recebem valores no momento em que são chamadas
    a = int(a)
    b = int(b)
    mult = a*b # Não retornam valores para quem as chamou
    print(f'{x} x {y} = {mult}')
# Função sem passagem de parâmetros e sem retorno
def dividir(): # Não recebem valores no momento em que são chamadas
    a = int(x)
    b = int(y)
    divisao = a/b # Não retornam valores para quem as chamou
    print(f'{x} / {y} = {divisao}')
# Programa Principal
x = int(input('Digite um número: ' ))
y = int(input('Digite mais um número:' ))
print(f'{x} + {y} = {somar(x,y)}')
diferenca = subtrair()
print(f'{x} - {y} = {diferenca}')
multiplicar(x,y)
dividir()