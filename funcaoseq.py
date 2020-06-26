# Função com entrada de parâmetros e sem retorno
def ordemcres(n1,n2,n3): # São inseridos valores no momento em que são chamadas
    numeros = [n1,n2,n3]
    print(sorted(numeros)) # Não retornam valores para quem as chamou
    # sorted: função do python que ordena os elementos da lista em ordem crescente
# Programa Principal
n1 = float(input('Informe um número:'))
n2 = float(input('Informe um segundo número:'))
n3 = float(input('Informe um terceiro número:'))
ordemcres(n1,n2,n3)