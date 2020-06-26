from cliente import Cliente
from conta import Conta
from cliente_conta import ClienteConta as cc
from banco import Banco

calil = Cliente('Calil Neves', '13-01-2001', '000.123.321-24')
rafa = Cliente('Rafael Santana', '14-01-1991','123.321.444-33')

conta001 = Conta('778','5046',500.00)
conta002 = Conta('111','2222',200.00)

calil001=cc(calil,conta001)
rafa002=cc(rafa,conta002)

real = Banco('Real Banck')
real.abrir_Conta(calil001)
real.abrir_Conta(rafa002)
real.clientes_contas[0].clie
real.clientes_contas[0].conta.extrato() #Mostra Extrato
real.clientes_contas[0].conta.saque(5)