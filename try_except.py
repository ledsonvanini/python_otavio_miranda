"""
    try, >> Tenta executar um trecho
    except, >> Se não conseguir captura uma excessão::
            >> Exception (Excessão mais genérica - BaseException)
            >> SyntaxError: invalid syntax
            >> ZeroDivisionError: division by zero
            >> NameError: name 'b' is not defined
            >> IndentationError: expected an indented block
            >> raise ValueError(<NomeDoErro>) a ser lançado pelo desenvolvedor
            >> Subclasses: ArithmeticError,
                           AssertionError,
                           AttributeError,
                           BufferError,
                           EOFError,
                           ImportError,
                           LookupError,
                           MemoryError,
                           NameError,
                           OSError, ...

    else,  >> Se não conseguir executa outro trecho
    finaly >> Finalmente executa o que estiver aqui (Independente de haver erro)
    Alias >> É possível dar um apelido para a excessão com a cláusula 'as' e.g.[Exception] as [Erro]
"""

from modulo.utils import pcomment
# name = 'Ledson'
# try:
#     print(name.find('0'))
# finally:
#
#     print('Não consegui...', Exception, TypeError.__name__, IndexError.__name__)
#     print(5*'-*-')
#     pp((Exception, TypeError.__name__, IndexError.__name__))
# print(15*'-')
# ## --------- DÁ ERRO ---------
# # try:
# #     print(2/5)
# # else:
# #     print('None...')
# ## --------- SEMPRE PRECISARÁ DE UM EXCEPT OU FINALLY ---------
#
#
# print(5*'-')
# try:
#     a = 2
#     b = 0
#     c = a / b
#     print(a[4])
#
# except Exception as errBase:
#     print(f'Grupo:: {BaseException(Exception)}' )
#     print(f'Err:: {Exception.__name__}' )
#     print(f'Erro Base:: {errBase}' )
# except NameError:
#     print(f'Err:: {NameError.__name__}')
# except (IndexError, TypeError ) as errInd:  # Alias + agrupamento de erros
#     print(f'INDEX:: {errInd }' )
# except ZeroDivisionError:
#     print(f'Err:: {ZeroDivisionError.__name__}')
#     print(f'Class:: {ZeroDivisionError.__class__.__name__}')
#
# finally:
#     print('Chegou ao fim')
#
# print(c)
pcomment('EXEMPLO COM RAISE')

def is_divisible(arg1, arg2):
    tipo_arg1 = type(arg1)
    tipo_arg2 = type(arg2)

    if arg2 == 0:
        raise ZeroDivisionError(f'\n>> Não consigo dividir por ZERO <<')
    if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
        raise TypeError(f'\n\t\t{arg1, arg2} Devem ser >> NÚMEROS << você enviou {tipo_arg1, tipo_arg2}')

    return True


def dividir(num, div):
    if is_divisible(num, div):
        print(num / div)

dividir(8,'0')
pcomment('')



