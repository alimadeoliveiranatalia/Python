print('Informe os seguints coeficientes de uma equação do segundo grau:')
a = float(input('Informe o valor de A:'))
b = float(input('Informe o valor de B:'))
c = float(input('Informe o valor de C:'))
delta = (b**2)-(4*a*c)
if delta<0:
    print('Não existe solução no conjunto dos Reais')
else:    
    x1 = ((-b)+(delta)**(0.5))/(2*a)
    x2 = ((-b)-(delta)**(0.5))/(2*a)
    print('A solução corresponde:')
    print('S = ', x1,',',x2)