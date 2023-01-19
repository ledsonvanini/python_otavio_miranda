import abc
import os

from modulo import pp, pl


class Conta(abc.ABC):
    def __init__(self, agencia: str, conta: str, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        pl()
        self.detalhes(f'SUCESSO \\O/, VALOR DEPOSITADO R${valor:.2f}')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'{msg}')
        print(f'SALDO ATUAL:: "{self.saldo:.2f}"')
        pl()


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        os.system('cls')
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque > 0:
            self.saldo -= valor
            self.detalhes(f'SUCESSO \\O/, VALOR DO SAQUE R${valor:.2f}')
            return self.saldo
        print(f'Não foi possível realizar o saque de R${valor:.2f}')
        return self.saldo


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r} {self.saldo!r})'
        return f'{class_name}: {attrs}'


class ContaCorrente(Conta):
    def __init__(self, agencia: str, conta: str, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        os.system('cls')
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SUCESSO \\O/, VALOR DO SAQUE R${valor:.2f}')
            return self.saldo
        print(f'Não foi possível realizar o saque de R${valor:.2f}')
        print(f'Seu limite é {-self.limite}')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r} {self.saldo!r} {self.limite!r})'
        return f'{class_name}: {attrs}'


if __name__ == '__main__':
    pp('POUPANÇA')
    cp1 = ContaPoupanca('0001', '1512', 1500)
    cp1.detalhes()
    cp1.sacar(100)
    cp1.sacar(1900)
    cp1.detalhes()

    pp('CORRENTE')
    cc1 = ContaCorrente('0002', '1612', 800, 150)
    cc1.detalhes()
    cc1.sacar(100)
    cc1.sacar(120)
    cc1.sacar(580)
    cc1.sacar(50)
    cc1.sacar(100)
    cc1.sacar(20)
    cc1.detalhes()
