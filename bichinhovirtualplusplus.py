class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, nome):
        self.nome = nome

    def alterar_fome(self, fome):
        self.fome = fome

    def alterar_saude(self, saude):
        self.saude = saude

    def alterar_idade(self, idade):
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_fome(self):
        return self.fome

    def get_saude(self):
        return self.saude

    def get_idade(self):
        return self.idade

    def humor(self):
        return self.get_fome() * self.get_saude()

    def alimentar(self, qtd):
        if (qtd >= 0) and (qtd <= 100):
            self.fome -= self.fome * (qtd / 100.0)

    def brincar(self, qtd):
        if (qtd >= 0) and (qtd <= 100):
            self.saude += self.saude * (qtd / 100.0)

    def str(self):
        return ('Nome: ' + str(self.get_nome()) + ', Fome: ' + str(self.get_fome()) + ', Saude: ' + str(
            self.get_saude()) + ', Idade: ' + str(self.get_idade()))


b = BichinhoVirtual('Tamagoshi', 8, 5, 12)
print(b.humor())
b.alimentar(50)
print(b.humor())
b.brincar(30)
print(b.humor())
print(b.str())
