mostrar_resultados=[]
for i in range(0,10):
    num = int(input('Informe um valor: ' ))
    par_ou_inpar = num%2
    if par_ou_inpar==0:
        mostrar_resultados.append([num,'é par'])
    else:
        mostrar_resultados.append([num,'é ímpar'])
for i in range(0,10):
    print(f'{i+1}.  {mostrar_resultados[i]}')