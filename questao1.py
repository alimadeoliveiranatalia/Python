estado = {}
contador = int(input('Informe quantas cidades queres registrar? '))
cidades = []

while contador<0:
    print('Informe apenas números inteiros maiores que zero')
    contador = int(input('Informe quantas cidades queres registrar? '))
estado2 = input('Informe um Estado: ')
for x in range(0,contador):
        cidades.append(input('Digite a cidade: '))
estado[estado2]= cidades
print(estado)
        
