idade = int(input('Informe sua idade, por favor'))
if idade <16:
    print('Pessoas com idades inferior à 16 anos, não são obrigados à votar')
if idade >=16 and idade<=60:
    print('Pessoas com idade superior à 16 e inferior à 60, são obrigados à votar')
if idade>60:
    print('Pessoas com idade superior à 60 anos, só votam por opção')