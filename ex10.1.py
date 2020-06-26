class Televisao:
    def __init__(self):
        self.ligada=False
        self.canal=2
        self.volume=20
        self.marca='Samsung'
    def muda_canal_baixo(self):
        if self.ligada:
            print('Estou desligada! :(')
            self.ligada=True
        else:
            self.canal-=1
            self.volume-=5
        print(f'Agora o canal é {self.canal} e seu volume está {self.volume}')
    def muda_canal_cima(self):
        if self.ligada:
            print('Estou desligada! :(')
            self.ligada=True
        else:
            self.canal+=1
            self.volume+=5
            print(f'Agora o canal é {self.canal} e seu volume está {self.volume}')
# Programa Principal
tv=Televisao() # Declara-se o objeto tv
print('Características do objeto tv')
#print(tv.ligada)
print(tv.canal)
print(tv.volume)
print(tv.marca)
tv.muda_canal_baixo()
tv_sala=Televisao() # Declara-se um outro objeto diferente de tv
tv_sala.ligada=True
tv_sala.canal=4
tv_sala.volume=40
tv_sala.marca='Semp'
print('Características do objeto tv_sala')
#print(tv_sala.ligada)
print(tv_sala.canal)
print(tv_sala.volume)
print(tv_sala.marca)
tv_sala.muda_canal_cima()