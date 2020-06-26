class Televisao: # classes são sempre definidas com letras maiúsculas
    def __init__(self): # Função construtora
        self.ligada = False
        self.canal=2
# Programa Principal
tv = Televisao() #Declara-se o objeto tv
tv.ligada
print(tv.ligada) # Mostrar o  valor do atributo tv na característica ligado
tv.canal
print(tv.canal) # Mostrar o  valor do atributo tv na característica canal