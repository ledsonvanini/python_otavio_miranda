from itertools import groupby
"""
    GroupBy 
        => Os dados precisam estar ordenados para agrupar corretamente
        
"""
alunos = [
    {'nome': 'Luiz', 'nota':'A'},
    {'nome': 'Maria', 'nota':'C'},
    {'nome': 'Anna', 'nota':'B'},
    {'nome': 'Pedro', 'nota':'A'},
    {'nome': 'Catia', 'nota':'A'},
    {'nome': 'Davi', 'nota':'C'},
]

# Agrupando Listas (Sempre ordenar primeiro)
# letras = ['a', 'a,', 'a', 'b','c', 'b']
# grupos = groupby(sorted(letras))
# # print(list(grupos))
# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))

## Agrupando Dicionários (Sempre ordenar primeiro)
filter_type = lambda a: a['nota']
sorted_alunos = sorted(alunos, key=filter_type)
grouped = groupby(sorted_alunos, key=filter_type)

def sortt(arr): ## Simulando o mesmo que foi feito em Sort coma Lambda Acima
    sort = []
    for a in arr:
        sort = sorted(a['nota'])
        print(f'{sort}')
    return sort
#sortt(alunos)

def agrupa(arr):
    sort = sortt(arr)
    pass
    # print(sort)


# print(sorted_alunos, sep='\n')
for chave, grupo in grouped:
    print(f'Alunos com nota "{chave}"')
    # print(list(grupo)) ## Neste caso podemos iterar sobre este grupo "GRUPO"
    for aluno in grupo:
        print(aluno)
    print()