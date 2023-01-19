"""
    Dataclasses: Decorator (Sintax sugar)

    Incluido na versão 3.7>

"""
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = sobrenome

if __name__ == '__main__':
    p1 = Pessoa('Jonatas', 'Martins')
    p1.nome_completo

    print(p1.nome)
    print(p1.sobrenome)
    print(p1.nome_completo)
