def somar(a,b):
    a = int(a)# converte os valores fornecidos em inteiros
    b = int(b)
    soma = a+b
    return soma
def subtrair(a,b):
    a = int(a)
    b = int(b)
    diferenca = a-b
    return diferenca
# Programa Principal que faz a soma e a diferença de dois números
c = input('Informe um valor, por favor' )
d = input('Informe um segundo valor, por favor')
resultado = somar(c,d)
resultado1 = subtrair(c,d)
print(f'{c} + {d} = {resultado}')
print(f'{c} - {d} = {resultado1}')
#def linha(): 
#    print('-'*60)


# Programa Principal
#linha()
#print('  Curso em Vídeo  ')
#linha()
#print('  Aprenda Python  ')
#linha()
#print('  Natália  ')
#linha()
#def titulo(txt):
#    print('-'*60)
#    print(txt)
#    print('-'*60)
#Programa Principal utilizando parâmetros
#titulo('  Curso em Vídeo  ')
#titulo('  Aprenda Python  ')
#titulo('    Natália    ')
