from functools import partial
from types import GeneratorType

"""
    PARTIAL
        > recebe uma Função e retorna uma Closure
        > Retorna um object alterado, mas geralmente com o mesmo tamanho (qtde de itens)
"""

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'celular', 'preco': 1850.00},
    {'nome': 'camiseta', 'preco': 150.00},
    {'nome': 'computador', 'preco': 6550.00},
    {'nome': 'mouse', 'preco': 150.00},
    {'nome': 'prensa', 'preco': 2550.00},
    {'nome': 'caneca', 'preco': 30.00},
]

def aumenta_percent(val, percent):
    return round(val * percent,2)

partial_func = partial (
    aumenta_percent, percent = 1.1
)
# produtos_alterados = [
#     {**p, 'novo_preco': p['preco'] * 1.5}  # Acrescenta 50% no preço do produto
#     for p in produtos
# ]

def aumentar_preco(produto):
    return {**produto,
            'novo_preco': produto['preco'] * 1.5
            }  # Acrescenta 50% no preço do produto


# novos_produtos = map(
#     aumentar_preco,
#     produtos
# )
## Para reutilizar o iterator Map basta convertê-la em uma List()
novos_produtos = list(map(
    aumentar_preco,
    produtos
))
print(f'Novos: {novos_produtos}\n')

## Ex.: Map, List e Lambda

list3 = list(map(lambda x: x * 3,[1,3,9,22]))

print(f'Multiplica x3: {list3}\n')

# produtos_alterados = [
# ]
#
#     {**p, 'novo_preco': partial_func(p['preco'])}  # Acrescenta 50% no preço do produto
#     for p in produtos
# ]

# print_iter(produtos_alterados)
print_iter(produtos)

print_iter(novos_produtos)
## Obs. 'novos_produtos map é um iterator Object'
print(novos_produtos)
print(hasattr(novos_produtos, '__init__')) # True
print(hasattr(novos_produtos, '__next__')) # True
print(isinstance(novos_produtos, GeneratorType)) # False
