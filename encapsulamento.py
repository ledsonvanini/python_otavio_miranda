
class Encapsulamento:
    def __init__(self):
        self._protec = '_Protected Method'
        self.__private = '_Get out'

    def _protected(self):
        return self._protec

    def __m_private(self, name= '__m_private'):
        print('Inside pivate', name)
        return self.__private

    def get_private(self):
        self.__m_private()

prot = Encapsulamento()

print(prot._protected())
# print(prot.__m_private())  # Impossível acessar
print(prot.get_private())  # Acessando por intermédio de um método público