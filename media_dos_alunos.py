# Armazenar as notas das avaliações parciais 1 e 2 de uma turma com 30 alunos. Criar uma lista com a média aritmética 
# das notas dos alunos. Informar quantos estão acima da média que é igual a 8 e informar a média da turma.
AL=3
parciais_nota1=[]
parciais_nota2=[]
media_da_parciais=[]
aprovados = []
for i in range(0,AL):
    parciais_nota1.append(float(input(f'Informe a nota {i+1} da parcial 1 : ' )))
for i in range(0,AL):
    parciais_nota2.append(float(input(f'Informe a nota {i+1} da parcial 2: ' )))
for i in range(0,AL):
    media_da_parciais.append((parciais_nota1[i]+parciais_nota2[i])/2)
    if media_da_parciais[i]>=8:
        aprovados.append(media_da_parciais[i])
media_da_turma = (sum(media_da_parciais))/AL
print(f'Notas da AV parcial 1: {parciais_nota1}')
print(f'Notas da AV parcial 2: {parciais_nota2}')
print(f'Média aritmética das 2 AVs: {media_da_parciais}')
print(f'Há {len(aprovados)} alunos aprovados')
print(f'A mádia da turma foi de: {media_da_turma}')