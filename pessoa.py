class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


le = Pessoa('Leandro', 32, 62, 175)
print(vars(le))
le.engordar(8)
print(vars(le))
le.emagrecer(12)
print(vars(le))
le.envelhecer(10)
print(vars(le))
le.crescer(2)
print(vars(le))
