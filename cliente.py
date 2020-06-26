class Cliente:
    def __init__(self, nome, data_nasc, cpf):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
    def status(self):
        print("""Nome: {}
Data Nascimento: {}
CPF: {}""".format(
            self.nome,
            self.data_nasc,
            self.cpf
            ))
