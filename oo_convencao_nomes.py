class Conta:
    _tipo_de_conta = (
        "corrente"  # Protegido, não deve ser acessadp diretamente fora da classe
    )
    __id_interno = 985645  # Privado, desencadeia name mangling

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0

    def depositar(self, value):
        self._saldo += value

    def sacar(self, value):
        self._saldo -= value
        return value

    def consultar(self):
        if self._saldo < 0:
            print("AVISO: Vocês está devendo")
        return self._saldo


conta = Conta(cliente="Ricardo")
