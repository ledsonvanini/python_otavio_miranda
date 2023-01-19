
import json

PATH = 'salvar_json_0.json'
class Pessoa:
    #ano_atual = 2022     # Attr da Class
    def __init__(self, nome, nasc):
        self.nome = nome
        self.nasc = nasc
        self.ano_atual = 2022

    def get_idade(self):
        return self.ano_atual - self.nasc

    def get_ano_nascimento(self):
        return self.ano_atual - self.get_idade()

joao = Pessoa('Joao', 1986)
anna = Pessoa('Anna', 1996)
maria = Pessoa('Maria', 2001)
print(joao.get_idade())
print(joao.get_ano_nascimento())

bd_json = [vars(joao), vars(anna), vars(maria)]

with open(PATH, 'w', encoding='utf8') as file:
    json.dump(bd_json, file, ensure_ascii=False, indent=4)

