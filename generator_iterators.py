"""
    # Iterator  iter(), next() => Qual o próximo valor?
    # Generator => São funções que sabem pausa em determinado ponto do código
        # Conhece o Next() element, mas não tem tamanho, não tem índice, não fica em memória
        # Yield é a palavra usada para pausar a função
"""

#from sys import getsizeof  ## Retorna o tamanho do item em Bytes
from time import sleep

# iterable = ['Maria', 'Xuxa', 'Nina']
# it = iter(iterable)
# print(next(it))
# print(next(it))
# print(next(it))

# lista = [n for n in range(5000)]
# generator = (n for n in range(5000))  # Generator "()"
#
# print(f'{getsizeof(lista ) } Bytes')
# print(f'{getsizeof(next(generator)) } Bytes')
#
# def generator(n=0):
#     yield 1  # Pausar
#     print('Primeira pausa...')
#
#     yield 2  # Pausar
#     print('Segunda pausa...')
#
#     yield 33  # Pausar
#     print('Terceira pausa...')
#
#     return  # Fim da função
# gen = generator(5)
# for g in gen:
#     print(g)

def meu_range(floor=0, roof=10):
    while True:
        yield floor
        sleep(1)
        floor += 1
        if floor >= roof:
            return
gen = meu_range(floor=1)  # precisa ser iterado
print(next(gen))
print(next(gen))
## ****** Ou.... *******
for g in gen:
    print(f'{g}s')
print('Goals reached \o/')
