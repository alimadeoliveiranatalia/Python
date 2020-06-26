valores = []
n=0
for x in range(0,3):
    valor = float(input('Informe um  valor'))
    valores.append(valor)
    n=n+1
if valores[0]<valores[1] and valores[0]<valores[2]:
    if valores[1]<valores[2]:
        print('[',valores[0],',',valores[1],',',valores[2],']')
    else:
        print('[',valores[0],',',valores[2],',',valores[1],']')
if valores[1]<valores[0] and valores[1]<valores[2]:
    if valores[0]<valores[2]:
        print('[',valores[1],',',valores[0],',',valores[2],']')
    else:
        print('[',valores[1],',',valores[2],',',valores[0],']')
if valores[2]<valores[0] and valores[2]<valores[1]:
    if valores[1]<valores[0]:
        print('[',valores[2],',',valores[1],',',valores[0],']')
    else:
        print('[',valores[2],',',valores[0],',',valores[1],']')