import os


class Carro:
    def __init__(self, nome, vel):  # Geralmente se usa 'self' para autoreferenciamento,
                                    # mas poderia ser outro termo
        self.nome = nome
        self.vel = vel
        self.max_vel = 120
        self.acc = 0.2

    def acelerar(self):
        if self.vel < self.max_vel:
            self.vel += self.vel * self.acc
        else:
            self.vel = self.max_vel
            print(f'Vai com calma "mocinha..."')
            print(f'Velocidade permitida 120km/h, você está a {self.vel}km/h')
            print(f'Reduced for security: {self.vel}')
            return

        print(f'VelAtual: {self.vel}')

        # os.system('cls')

fusca = Carro('Fusca', 80)
print(f'Vel Inicial {fusca.vel}')
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
fusca.acelerar()
