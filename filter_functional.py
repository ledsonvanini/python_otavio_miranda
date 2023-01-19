
from modulo import print_iter, pcomment
"""
    FILTER
        > Filtro funcional
        > Retorna um object, geralmente menor q o original (filtrado)
"""

produtos = [
    {'nome': 'celular', 'preco': 1850.00},
    {'nome': 'camiseta', 'preco': 150.00},
    {'nome': 'computador', 'preco': 6550.00},
    {'nome': 'mouse', 'preco': 150.00},
    {'nome': 'prensa', 'preco': 2550.00},
    {'nome': 'caneca', 'preco': 30.00},
]

## Exemplo com list Comprehension
# filter_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]

## Exemplo com Filter Funcional
filter_funcional = filter(lambda x: x['preco'] > 5000, produtos)

# print(filter_produtos, sep='\n')
# print(*list(filter_produtos), sep='\n\n')
# print_iter(filter_produtos)
print_iter(filter_funcional)
