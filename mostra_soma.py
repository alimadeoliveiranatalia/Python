numeros = []
TAM = 20
for i in range(0,TAM):
    numeros.append(int(input(f'Informe o valor {i+1} da lista: ' )))
print(sum(numeros)) # sum: Função que soma os elementos numéricos da lista