class Funcionario:
    def __init__(self,salario):
        #self.opcao=opcao
        self.salario=salario
    def menu(self):
        print('1. Imposto')
        print('2. Novo Salário')
        print('3. Classificação')
    def calcula_imposto(self):
        if self.salario<500:
            imposto=self.salario*0.05
            print(f'O imposto é de: R${imposto}')
        elif self.salario>=500 and self.salario<850:
            imposto=self.salario*0.1
            print(f'O imposto é de: R${imposto}')
        elif self.salario>=850:
            imposto=self.salario*0.15
            print(f'O imposto é de: R${imposto}')
    def calcula_novo_salario(self):
        if self.salario>1500:
            salario_com_aumento=self.salario+25
            print(f'Seu novo salário é de R${salario_com_aumento}')
        elif salario>=750 and salario<=1500:
            salario_com_aumento=salario+50
            print(f'Seu novo salário é de R${salario_com_aumento}')
        elif salario>=450 and salario<750:
            salario_com_aumento=salario+75
            print(f'Seu novo salário é de R${salario_com_aumento}')
        elif salario<=450:
            salario_com_aumento=salario+100
            print(f'Seu novo salario é de R${salario_com_aumento}')
    def classificar(self):
        if salario<=750:
            print('Você está sendo mal remunerado!')
        else:
            print('Você é bem remunerado!')    