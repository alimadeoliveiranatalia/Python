# Programa que lê 50 posições de números inteiros e mostra sommente os positivos
positivos = []
TAM = 50
for i in range(0,TAM):
    num = int(input(f'Informe o valor {i+1} da lista: ' ))
    if num>0:
        positivos.append(num)
print(positivos)