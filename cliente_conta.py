class ClienteConta:
    def __init__(self,cliente,conta):
        self.cliente=cliente
        self.conta=conta
    def geral(self):
        self.cliente.status()
        self.conta.extrato()
    def depositar(self,valor):
        self.conta.deposito(valor)
    def sacar(self,valor):
        self.conta.saque(valor)