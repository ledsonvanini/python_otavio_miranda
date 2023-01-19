
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, val):
        self._motor = val

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, val):
        self._fabricante = val



class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.fabricante = Fabricante(self.nome)


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

tesla = Carro('Tesla')
motor_m3 = Motor('M34S1')
tesla = Fabricante('Tesla Motors')
tesla.fabricante = tesla
tesla.motor = motor_m3
#----------------------------------
carro = Carro('Tesla')
motor_m3 = Motor('M34S1')
tesla = Fabricante('Tesla Motors')
carro.fabricante = tesla
carro.motor = motor_m3

print(f'Marca: {carro.nome}')
print(f'Fabricante: {carro.fabricante.nome}')
print(f'MOtor: {carro.motor.nome}')