from abc import ABC


class Conta(ABC):
    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0  # privado, com 2 unders se torna privado e classe filha não poderá acessar


class ContaCorrente(Conta):
    __id_interno = 985645  # Privado, desencadeia name mangling

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0  # protegido

    @property  # getter
    def saldo(self):
        if self._saldo < 0:
            print("AVISO: Vocês está devendo")
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo += value

    @saldo.deleter
    def saldo(self):
        self._saldo = 0


conta = ContaCorrente(cliente="Ricardo")
print(conta.cliente)
print(conta.saldo)

# deposito
conta.saldo = 100
print(conta.saldo)
conta.saldo = 200
print(conta.saldo)

# saque
conta.saldo = -50
print(conta.saldo)

# reiniciar a conta
del conta.saldo
print(conta.saldo)
