"""

"""
# Relembrando Desempacotamento
# a, b = 1, 2
# b, a = a, b
# print(a,b)
# print(b,a)
# *************************
#a,b = pessoa  # Retorna as chaves 'Nome e sobrenome'
#a,b = pessoa.values() retorna o valor das chaves 'Nome e Sobrenome'
# a,b = pessoa.items()  # Retorna uma tupla com nome e sobrenome
# print(a,b)
#
# (a1, a2), (b1,b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
#
# for key, value in pessoa.items():
#     print(f'{key}: {value}')

# ******UNINDO DICIONÁRIOS **************************
pessoa = {
    'nome': 'Ledson',
    'sobrenome': 'Vanini'
}
dados_pessoa = {
    'idade': 36,
    'logradouro': 'Bairro alto, 245'
}
pref_food = ['Arroz', 'Salada', 'Carnes']
## Extração de dicionarios dentro de outros dicionários
## Com o operador '**'
## Pode-se adicionar key/value a mais
## Não dá pra desenpacotar listas, tuplas e sets em dicionários
# (TypeError: 'set' object is not a mapping)

# logradouro = {**pessoa, **dados_pessoa, 'numero': '245', 'bairro': 'alto'}
# print('------\n', logradouro)

#********* Funções com Kwargs (Parametros nomeados)*************************
def dados_nomeados(*args, **kwargs):
    print(f'Não nomeados {args}')
    for key, value in kwargs.items():
        print(key, value)

## dados_nomeados(32, 'Meia idade', 'Zac', 'Cachorrinho', **pessoa) # Possível extrair um dict
## dados_nomeados(nome='Ledson', idade='32') // ou passar os dados diretamente




