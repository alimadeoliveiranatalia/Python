# Programa que armazena uma sequência de 5 valores inteiros e mostra o menor maior valor
TAM = 5
valores = []
for i in range(0,TAM):
    valores.append(int(input(f'Informe o valor {i+1} da lista ' )))
print(f'O maior número é: {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor número é: {min(valores)} na posição {valores.index(min(valores))}')


