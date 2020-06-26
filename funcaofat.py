# Função com entrada de parâmetros e com retorno
def fatorial(num): # Recebe valores no momento em que é chamanda
    num = int(num)
    fat = 1
    if num < 0:
        return ('Não existe fatorial de número negativo.') # retorna valores para quem a chamou 
    elif num ==0:
        return ('O fatorial de 0!=1')
    else:
        for i in range(num,0,-1):
            fat*=i
        return fat # Retornam valores para quem as chamou
#num = int(input('Informe um valor: '))
#print(fatorial(num))