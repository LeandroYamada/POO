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


class ContaInvestimento(ContaCorrente):
    def __init__(self, numero, nome, saldo, taxajuros):
        ContaCorrente.__init__(self, numero, nome, saldo)
        self.taxajuros = taxajuros

    def adicione_juros(self):
        self.saldo += (self.saldo * self.taxajuros / 100)


poupanca = ContaInvestimento(225, "Leandro", 1000, 10)
print(vars(poupanca))
poupanca.adicione_juros()
poupanca.adicione_juros()
poupanca.adicione_juros()
poupanca.adicione_juros()
poupanca.adicione_juros()
print(vars(poupanca))
