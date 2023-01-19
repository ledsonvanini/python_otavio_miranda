from modulo import pcomment
from itertools import zip_longest
#
# cidades = ['Curitiba', 'São Paulo', 'Floripa']
# estados = ['Paraná', 'São Paulo', 'Santa Catarina']
#
# for cities in zip(cidades, estados):
#     list_cities = tuple(cities)
#     print(list_cities, sep='\t')
#
# new_cities = [
#     {'cidade': c, 'estado':e}
#     for c, e in zip(cidades, estados) if c.startswith('C')]
# print(new_cities)
#

cidades_br = ['Curitiba', 'São Paulo', 'Floripa']
estados_br = ['PR', 'RO', 'SP', 'MA', 'SC']

pcomment('Função Zipper')

def zipper(cidades, estados):
    max_interval = min(len(cidades), len(estados))
    return [
        (estados[i], cidades[i] )
        for i in range(max_interval)
    ]

print(zipper(cidades_br, estados_br))
# Alternativamente "ZIP() retorna um Iterator"
print(list(zipper(cidades_br, estados_br)))
# From Itertools "ZIP_LONGEST() Iterator da maior lista analisada"
print(list(zip_longest(cidades_br, estados_br)))
