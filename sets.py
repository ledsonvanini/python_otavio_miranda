#https://docs.python.org/3.11/library/stdtypes.html#set-types-set-frozenset
""""
 > Retorna um Conjunto de iteraveis, não repetidos
    Sets can be created by several means:
        Use a comma-separated list of elements within braces: {'jack', 'sjoerd'}
        Use a set comprehension: {c for c in 'abracadabra' if c not in 'abc'}
        Use the type constructor: set(), set('foobar'), set(['a', 'b', 'foo'])
 > Não tem índices
 > Não garantem a ordem dos elementos
 > São iteráveis [ for, in, not in, while]

"""
# string = 'Luiz otavio'
# set_str = set(string)
# i = 0
# for ind in set_str:
#     print(ind)  # Retorna conjunto de elementos em onderm aleatória
# # while i <= len(set_str):
# #     print(set_str)
# #     i += 1
# print(type(set_str))  # Type Set
# #print(set_str)        # Printa um Set

# *******************************************
# Convertendo lista em Sets e Vice-Versa
numb = [1,2,3,242,2,'Mariah',2,2,2,3,23,1]
is_list = {1,23,3,'Jon',22}  # Criar diretamente um SET
n_numb = list(set(numb))  # 1 - Removidos os numeros repetidos
                          # 2 - Reconvertido para uma lista
                          # 3 -  (Sem indeces)
print(set(n_numb))  # Desordenado e aleatório (Sem indeces)
print(type(n_numb))
print(f' Is: {type(is_list)})')
print(is_list.update(('Martha',)))
print(is_list)
print(is_list.clear()) ## Limpa todos os itens
# print(is_list.discard('Mariah')) ## Limpa itens específicos
print('Limpando...')
print(is_list)
# *******************************************
"""
 Operadores para Sets:
 > União '|' - Unions
 > Interseção '&' - Itens presentes em ambos
 > Diferença '-' Itens presentes em apenas um dos Sets
 > Diferença '^' Simétrica - Itens que não estão em ambos 
 
"""

s1 = {1,2,3,5}
s2 = {2,3,23,5}
print(s1 | s2)  # Union
print(s1 & s2)  # Intersection
print(s1 - s2)  # Diferença (priodide item mais à esquerda)
print(s1 ^ s2)  # Diferença Simétrica - Itens únicos em cada conjunto




