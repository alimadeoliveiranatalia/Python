soma = 0
for x in range(0,3):
    nota = float(input('Digite nota: '))
    while nota<0 or nota>10:
        print('Não existe nota negativa e nem maior que 10')
        nota = float(input('Digite nota: '))
    soma = soma+nota
    media = soma/3
if media>=7:
    print('Sua média foi {}, aprovado'.format(media))
else:
    print('Sua média foi {}, reprovado'.format(media))
    