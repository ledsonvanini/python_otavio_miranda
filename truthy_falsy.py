"""
    truthy_falsy, tipos mutáveis e imutáveis
    Mutáveis: {}, [], set()
    Imutáveis: 0.0, "", range(0,10), None, False
"""
import pprint
def pp(valor):
    pprint.pprint(valor, indent=2, width=80)

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'is Falsy' if not valor else 'is Truthy'

pp(falsy(lista))
pp(falsy(dicionario))
pp(falsy(conjunto))
pp(falsy(tupla))
pp(falsy(string))
pp(falsy(flutuante))
pp(falsy(nada))
pp(falsy(falso))
pp(falsy(intervalo)) ## Apenas se o intervalo estiver vazio