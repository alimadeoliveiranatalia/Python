class meu_objeto:
    def __init__(self): # metodo construtor (inicializa o objeto)
        self.nome = 'Natália'
        self.idade = 27
        print('Construtor foi chamado com sucesso')
    def imprime(self):
        print(f'Olá meu nome é {self.nome} e eu tenho {self.idade} anos')
# Até aqui já foi criada a classe meu_objeto
Natalia = meu_objeto() # declara-se o objeto Natalia
Natalia.imprime()

