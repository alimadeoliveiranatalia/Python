nota1 = float(input('Informe a primeira nota obtida'))
nota2 = float(input('Informe a segunda nota obtida'))
nota3 = float(input('Informe a terceira nota obtida'))
media = (nota1+nota2+nota3)/3
print(media)
if media >= 7:
    print('Aprovado, parabêns')
else:
    print('Reprovado, infelizmente.')