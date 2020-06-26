numeros = []
TAM = 10
for i in range(0,TAM):
    numeros.append(int(input(f'informe o {i+1}. valor: ')))
num = int(input('Informe um valor. Please. ' ))
#numeros.sort() # ordena oa elementos da lista em ordem crescente
#numeros.sort(reverse=True) # ordena os elemntos da lista em ordem decrescente
#numeros.insert(3,24) # insere na posição 3 da lista o numero 24
print(numeros)
#numeros.pop(2) # elimina o elemento na posição 2 da lista
print(f'Existem {len(numeros)} elementos') # len: função que mostra o total de elementos da lista
#numeros.remove(2) # elimina o elemento na posição 2 da lista
if num in numeros: # se num estiver dentro de lista faça:
    print(f'Tenho {num} na lista')
else:
    print(f'Não tenho {num} na lista')
