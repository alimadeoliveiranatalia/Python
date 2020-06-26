# Programa que lê uma lista de 80 posições mostrando os elemnetos que são multiplos de 6 e suas posições
ATE = 3
numeros = []
so_mult6 =[]
posicoes_mult6 = []
for i in range(0,ATE):
    numeros.append(int(input(f'Informe o valor {i+1} para a lista ' )))
    if numeros[i]%6==0:
        so_mult6.append(numeros[i])
for i in range(0,ATE):
    if numeros[i]%6==0:
        posicoes_mult6.append(numeros.index(numeros[i]))
print(f'temos {len(so_mult6)} numeros que são mutiplos de 6')
print(f'Nas posições {posicoes_mult6} da lista {numeros}. problema resolvido :)')



