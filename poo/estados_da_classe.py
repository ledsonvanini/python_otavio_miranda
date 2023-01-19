from modulo.utils import cls


class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando ;)')
            cls()
            return
        else:
            self.filmando = True
            print(f'{self.nome} agora está filmando')


    def parar_filmagem(self):
        if self.filmando:
            print(f'{self.nome} filmagem stopada')
            self.filmando = False
        else:
            print(f'{self.nome} deseja filmar?')



    def fotografar(self):
        if self.filmando is True:
            print(f'o modelo {self.nome} não é capaz de fotografar enquanto filma:(')
        else:
            print(f'{self.nome} fala "X"')



c1 = Camera('Canon A52')
c2 = Camera('Sony EW3')
c1.fotografar()
c1.filmar()
c1.parar_filmagem()
c1.fotografar()
print(c1.filmando)
print(c2.filmando)

