"""
    Static Method:
        - Não conhece nada sobre a Class ou Instancias
        - Pode lidar apenas com seus atributos
        - útil apenas quando precisamos criar (UTILITIES ->E.g. date.replace('/', '-'))
"""

class Carro:
    def __init__(self):
        ...

    @staticmethod
    def estatico(self, *args, **kwargs):
        print('Static...')
        print(args)
        print(kwargs)

c1 = Carro
c1.estatico(25)