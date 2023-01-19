"""
    https://docs.python.org/3.11/tutorial/datastructures.html?highlight=list%20comprehension
    # LIST COMPREHENSION > Forma rápida de criar listas a partir de iteráveis
    # Pode ser obtida através de uma expressão lambda, if ternário, um cálculo etc
"""
# print(list(range(10))) # Cria uma lista de 0 a 9
## **** Old School and List Comprehension way *****
    # lista = []
    # for i in range(10):
    #     lista.append(i*2)
#     # print(lista)
# lista1 = [
#     number for number in range(10)
# ]
# ## À esquerda do 'for' colocamos o que deverá ser adicionado à variável
# ## Poder apenas o iterável (num) em questão ou uma lógica (ex. num**2)
# lista = [
#     number if number % 2 == 0 else 'Impar'
#     for number in range(10)
# ]
# print(lista)
# print(lista1)
## **********************
## **** Mapeando dados in List Comprehension *****

import pprint

def pp(p):
    pprint.pprint(p, width=80, indent=2, compact= True)

nomes = ['JOão', 'Maria', 'Catia', 'Davi']

produtos = [
    {'nome': 'Coca-Cola', 'preço': 35.5},
    {'nome': 'Allstar', 'preço': 250.0},
    {'nome': 'Ração', 'preço': 23.5},
    {'nome': 'Celular', 'preço': 1980.5},
]

# produtos_map = [
#     produto['nome']
#     for produto in produtos
# ]
# print(produtos_map)
produtos_map = [
    {**produto, 'n_preço': (produto['preço'] * 1.5) -(produto['preço'])}
     for produto in produtos
]
# print(*produtos_map, sep='\n')
# pp(produtos_map)
# print(f'{15*"👇-👆-"}')
# pp(produtos)

## *********** FILTROS ************
# print(f'{15*"👇-👆-"}')
# num_list = [
#     num for num in range(10) if num % 2 == 0  # Nesse caso o Filtro é o If após o For
# ]
# print(num_list)
# pp(num_list)

## *********** Nested For Statement ************
#lista2 = []
# for x in range(3):
#     for y in range(3):
#         lista2.append((x,y))  # Old School way
# pp(lista2)
lista2 = [
    (x, z, y)
    for x in range(2)
    for z in range(3)
    for y in range(3)   # With Comprehension List
    if x or y or z > 0  # If no final é FILTRO
]

l = (x ** 2 for x in range(10))
pp(repr(l))

