dia = int(input('Informe o dia em que você nasceu, por favor'))
mes = int(input('Informe o mes em que você nasceu, por favor'))
if mes == 1:
    mes_aniversaio = 'Janeiro'
if mes == 2:
    mes_aniversaio = 'Fevereiro'
if mes == 3:
    mes_aniversaio = 'Março'
if mes == 4:
    mes_aniversaio = 'Abril'
if mes == 5:
    mes_aniversaio = 'Maio'
if mes == 6:
    mes_aniversaio = 'Junho'
if mes == 7:
    mes_aniversaio = 'Julho'
if mes == 8:
    mes_aniversaio = 'Agosto'
if mes == 9:
    mes_aniversaio = 'Setembro'
if mes == 10:
    mes_aniversaio = 'Outubro'
if mes == 11:
    mes_aniversaio = 'Novembro'
if mes == 12:
    mes_aniversaio = 'Dezembro'
ano = int(input('Informe o ano em que você nasceu, por favor'))
hora = int(input('Informe a hora em que você nasceu, por favor'))
minu = int(input('Informe os minutos em que você nasceu, por favor'))
print('Você nasceu em:', dia, '/', mes_aniversaio, '/', ano, 'as', hora,':',minu)