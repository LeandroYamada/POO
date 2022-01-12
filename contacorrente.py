class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0.0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome_correntista = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor


c = ContaCorrente('1', 'Leandro', 155.0)
print(vars(c))
c.alterar_nome('Alexandre')
c.deposito(50)
print(vars(c))
c.saque(10)
print(vars(c))
