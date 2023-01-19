# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum
from enum import Enum
# import enum

Directions = Enum('Directions', ['LEFT', 'RIGHT', 'UP', 'DOWN'])  #Convenção MAIUSC. PARA CONSTs


def mover(direcao: Directions):
    if not isinstance(direcao, MyEnum):
        raise ValueError(f'Valor não localizado')

    print(f'Movendo para {direcao.name}')

# mover('esquerda')
# mover('direita')
# mover('acima')
# mover('abaixo')

# mover(Directions.UP)
# mover(Directions.DOWN)
# mover(Directions.LEFT)
# mover(Directions.RIGHT)
# # Chamando o Enum por indexes
# print(Directions(1), Directions['LEFT'], Directions.UP)  # Chama o membro inteiro
#
# print(Directions(1).name)   # Chama pelo Nome
# print(Directions(1).value)  # Chama pelo Valor

# Abordagem mais comum é criar uma class Enum
class MyEnum(Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()

mover(MyEnum.UP)