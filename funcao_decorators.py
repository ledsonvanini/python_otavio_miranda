from modulo import *

"""
    Decorators: Podem ser vistas como Factory Functions
    ou seja, funções que criam ou tratam a execução de outras funções
"""

# def criar_funcao(func):
#     def interna(*args, **kwargs):
#         print('Começo do decorator...')
#         for arg in args:
#             eh_string(arg)
#         res = func(*args, **kwargs)
#         print('Decorated...')
#         return f'Resultado: "{res}"'
#     return interna
#
# def invert_string(str):
#     return str[::-1]
#
# def eh_string(param):
#     if not isinstance(param, str):
#         raise TypeError('[Param] deve ser uma [string]')
#
# inverte_checando = criar_funcao(invert_string)
# invertida = inverte_checando('Maria')
# print(invertida)

# pcomment('SintaxSugar Decorator')
#
# def criar_funcao(func):
#     def interna(*args, **kwargs):
#         print('Começo do decorator...')
#         for arg in args:
#             eh_string(arg)
#         res = func(*args, **kwargs)
#         print('Decorated...')
#         return f'Resultado: "{res}"'
#     return interna
#
# @criar_funcao
# def invert_string(str):
#     print(f'Nome da Função decorada: "{invert_string.__name__}"')
#     return str[::-1]
#
# def eh_string(param):
#     if not isinstance(param, str):
#         raise TypeError('[Param] deve ser uma [string]')
#
# invertida = invert_string('Maria')
# print(invertida)

pcomment('Decorators com Parametros')

def _decorator(func):
    print('Decorating 1...')
    def inner_function(*args, **kwargs):
        print('Nesting...')
        res = func(*args, **kwargs)
        print('Decorated...')
        return f'Your Result: "{res}"'
    return inner_function

@_decorator
def soma(x, y):
    print(f'Function Decorator > "{soma.__name__}"')
    return x + y

dez_mais_cinco = soma(10,5)


print(dez_mais_cinco)