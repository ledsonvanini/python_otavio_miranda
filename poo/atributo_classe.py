
# Atributos da classe
class Pessoa:
    #ano_atual = 2022     # Attr da Class
    def __init__(self, nome, nasc):
        self.nome = nome
        self.nasc = nasc
        self.__ano_atual = 2022

    def get_idade(self):
        return self.__ano_atual - self.nasc

    def get_ano_nascimento(self):
        return self.__ano_atual - self.get_idade()

joao = Pessoa('Joao', 1986)
print(joao.get_idade())
print(joao.get_ano_nascimento())
print(joao.__dict__)  # Dander dict permite ler e alterar atribunos públicos
joao.__dict__['nome'] = 'Pedro'
#vars(joao.nome) = 'Ledson' Erro ao tentar atribuir
print(joao.__dict__)
print(vars(joao))
# Proibido
## print(joao.__ano_atual)