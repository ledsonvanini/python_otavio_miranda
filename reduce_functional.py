from functools import reduce

from modulo import print_iter, pcomment
"""
    REDUCE
        > Reduzir um iterável a um único valor
        > 
"""

produtos = [
    {'nome': 'celular', 'preco': 1850.00},
    {'nome': 'camiseta', 'preco': 150.00},
    {'nome': 'computador', 'preco': 6550.00},
    {'nome': 'mouse', 'preco': 150.00},
    {'nome': 'prensa', 'preco': 2550.00},
    {'nome': 'caneca', 'preco': 30.00},
]

## Old school example (somar todos os preços)
# preco_soma = 0
# for p in produtos:
#     preco_soma += p['preco']
## Alternativamente sum()
# print(sum(p['preco'] for p in produtos))



## Functional Reduce example (somar todos os preços)



print()
