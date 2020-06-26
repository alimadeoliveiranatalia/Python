lista_a = []
lista_b = []
lista_c = []
receba = int(input('Informe um tamanho para lista'))
while receba<=0:
    print('Informe apenas valores inteiros maiores que zero')
    receba = float(input('Informe um tamanho para a lista: '))
for y in range(0,receba):
    lista_a.append(float(input('Informe os elementos para a 1ª lista')))
print('A =',lista_a)
for x in range(0,receba):
    lista_b.append(float(input('Informe os elementos para a 2ª lista')))
print('B =',lista_b)
n=0
for z in range(0,receba):
    valor = lista_a[n]*lista_b[n]
    n=n+1
    lista_c.append(valor)
print('C =',lista_c)