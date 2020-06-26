numeros = []
cont = 0
for x in range(0,5):
    num = float(input('Informe valores:'))
    numeros.append(num)
    cont =cont+1
#    while numeros[0]==numeros[1] or numeros[0]==numeros[2] or numeros[0]==numeros[3] or numeros[0]==numeros[4]:
#        print('Não é possível que os números se repitam.')
#        num = float(input('Informe valores:'))   
#    while numeros[1]==numeros[0] or numeros[1]==numeros[2] or numeros[1]==numeros[3] or numeros[1]==numeros[4]:
#        print('Não é possível que os números se repitam.')
#        num = float(input('Informe valores:'))   
#    while numeros[2]==numeros[0] or numeros[2]==numeros[1] or numeros[2]==numeros[3] or numeros[2]==numeros[4]:
#        print('Não é possível que os números se repitam.')
#        num = float(input('Informe valores:'))   
#    while numeros[3]==numeros[0] or numeros[3]==numeros[1] or numeros[3]==numeros[2] or numeros[3]==numeros[4]:
#        print('Não é possível que os números se repitam.')
#        num = float(input('Informe valores:'))    
#    while numeros[4]==numeros[0] or numeros[4]==numeros[1] or numeros[4]==numeros[2] or numeros[4]==numeros[3]:
#        print('Não é possível que os números se repitam.')
#        num = float(input('Informe valores:'))    

if numeros[0]>numeros[1] and numeros[0]>numeros[2] and numeros[0]>numeros[3] and numeros[0]>numeros[4]:
    print('O maior número é',numeros[0])
if numeros[1]>numeros[0] and numeros[1]>numeros[2] and numeros[1]>numeros[3] and numeros[1]>numeros[4]:
    print('O maior número é',numeros[1])
if numeros[2]>numeros[0] and numeros[2]>numeros[1] and numeros[2]>numeros[3] and numeros[2]>numeros[4]:
    print('O maior número é',numeros[2])
if numeros[3]>numeros[0] and numeros[3]>numeros[1] and numeros[3]>numeros[2] and numeros[3]>numeros[4]:
    print('O maior número é',numeros[3])
if numeros[4]>numeros[0] and numeros[4]>numeros[1] and numeros[4]>numeros[2] and numeros[4]>numeros[3]:
    print('O maior número é',numeros[4])