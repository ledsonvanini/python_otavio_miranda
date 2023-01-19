
class Pessoa:
    ano = 2023  # Atributo da Classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # Decorator de Classe para chamar métodos exclusivos da Classe (exige 'cls' como param)
    def say(cls):
        print('Saying Hello')

    @classmethod
    def criar_cinquentao(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls(idade, 'noname')


joao = Pessoa('João', 36) # Métodos de instancia
maria = Pessoa.criar_cinquentao('Maria') # Criado com classmethod (Factory)
anonima = Pessoa.criar_sem_nome(25)
joao.say()
print(Pessoa.ano)

print(anonima.idade)
print(anonima.nome)
# print(maria.nome)
# print(maria.idade)
# Pessoa.say()