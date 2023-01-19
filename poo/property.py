"""
    PROPERTY:
        - É um decorator @property
        - É o Getter do Python ('pythonico')
        - É um método que se comporta como um atributo (Sem Parentese)
"""

class Caneta:
    def __init__(self, cor='Azul-Caneta'):
        self._cor = cor

    @property             # Método que se comporta como atributo
    def cor(self):        # (Ao invés de <instancia>.attr(value) <=> <instancia.attr = value>)
        return self._cor

    @cor.setter            # Método que se comporta como atributo    #
    def cor(self, value):  # (Ao invés de <instancia>.attr(value) <=> <instancia.attr = value>)
        self._cor = value


bic = Caneta()
print(Caneta.cor)
print(bic.cor)
# bic.cor = 'Verde'
print(bic.cor)