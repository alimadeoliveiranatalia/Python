class Banco:
    def __init__(self,nome):
        self.nome=nome
        self.clientes_contas=[]
    def listarClientes(self):
        for cliente in self.clientes_contas:
            cliente.geral()
    def abrir_Conta(self,dados):
        self.clientes_contas.append(dados)
    def fechar_Conta(self,pos):
        self.clientes_contas.pop(pos)
