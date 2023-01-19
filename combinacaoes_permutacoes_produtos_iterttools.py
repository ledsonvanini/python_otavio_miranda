from itertools import permutations,combinations, product
from time import sleep

"""
    >> FROM Itertools
        Combinations  => Combinações Simples
        Permutations  => Todas as combinações possíveis
        Products      => Cria um novo produtos (Cartesiano)
    - Obs.: Caso eu tenha um iterator sempre vou ter que esgotá-lo (For, white, etc)
"""

pessoas = [
    'Joao','Maria', 'Pedro','Ledson'
]
camisetas = [
    ['branca', 'preta', 'azul'],
    ['M', 'F'],
    ['P', 'M','G'],
]

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
#
# print_iter(combinations (pessoas, 2))
# print_iter(permutations (pessoas, 2))
print_iter(product (*camisetas))
