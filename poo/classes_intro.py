"""
    > CLASSES
        - Classes são moldes que geram 'novos' objetos ou instancias
        - Objetos tem seus próprios atributos e métodos
        - Para o nome de classes usa-se a convenão PascalCase
        - Em Python o nome do arquivo não precisa ser igual ao nome da Class como acontece com 'Java' por ex.
        - ATRIBUTOS DA CLASSE = Dados (nome, peso, cor etc)
        - MÉTODOS DA CLASSE = Ações, verbos (andar, acelerar, comer etc)
        - __init__ É um método inicializador de atributos da classe (Garante que cada instancia seja única - self)

"""
from poo.metodos import Carro
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

joao = Pessoa('João', 'Arruda')

print(joao.nome)  # <__main__.Pessoa object at 0x000002347F4D37D0> =>> NOME DA CLASSE / LOCAL DA MEMÓRIA

