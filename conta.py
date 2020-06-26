class Conta:
    def __init__(self, numero, agencia, saldo = 0.0):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.transacoes = []
    def extrato(self):
        print("""Conta: {}
Agencia: {}
Saldo: R${}""".format(
            self.numero,
            self.agencia,
            self.saldo
            ))
        for t in self.transacoes:
            print('{}R${:.2f}'.format(t[0],t[1]))
    def deposito(self, valor_deposito):
        if valor_deposito>0:
            self.saldo+=valor_deposito
            self.transacoes.append(['deposito - +',valor_deposito])
            print('deposito efetuado com sucesso!')
        else:
            print('valor de deposito inválido')
    def saque(self, valor_saque):
        if valor_saque>0 and self.saldo>valor_saque:
            self.saldo-=valor_saque
            self.transacoes.append(['saque - -',valor_saque])
            print('saque efetuado com sucesso')
        else:
            print('ocorreu um erro!')