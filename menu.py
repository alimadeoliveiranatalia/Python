# Menu que insere e apaga elementos de uma lista
pessoas = []
opcao = 5
while opcao!=4:
    print('[1] - Inserir Pessoa')
    print('[2] - listar ')
    print('[3] - Apagar')
    print('[0] - Sair')
    opcao = int(input('Digite uma opção: ' ))
    while opcao<0:
        print('Não existe opção disponível para o dígito escolhido')
        opcao = int(input('Digite uma opção: ' ))
    if opcao==1:
        pessoas.append(input('Digite o nome da pessoa que deseja inserir: ' ))
    elif opcao==2:
        print(pessoas)
    elif opcao==3:
        pessoas.remove(input('Informe o nome que você gostaria de apagar: ' ))
        print('O nome foi excluído. Tecle 2 para verificar.')
    elif opcao==0:
        opcao=4
print('Fim ')