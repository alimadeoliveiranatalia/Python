# programa que lê 80 elementos inteiros, encontra e mostra o menor elemento e sua posição
TAM = 5
numeros = []
for i in range(0,TAM):
    num = int(input(f'Informe o valor {i+1} : ' ))  
    numeros.append(num)
print(f'O menor valor é {min(numeros)}') # min: função que mostra o menor elemento da lista
print(f'E sua posição é {(numeros.index(min(numeros)))} na lista') # index: função que mostra a posição do elemento na lista
#valores = []
#valores.append(5)
#valores.append(4)
#valores.append(9)
#for c,v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Chegeui ao final da lista')