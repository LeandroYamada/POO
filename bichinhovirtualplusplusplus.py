from random import randint


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


p = BichinhoVirtual('Papagaio', randint(0, 10), randint(0, 10), 4)
c = BichinhoVirtual('Coelho', randint(0, 10), randint(0, 10), 8)
g = BichinhoVirtual('Galinha', randint(0, 10), randint(0, 10), 5)
fazenda = [p, c, g]

while True:
    print('--- FAZENDA ---')
    print('1. Alimentar todos os bichos')
    print('2. Brincar com todos os bichos')
    print('3. Ouvir todos os bichos')
    print('4. Sair')
    op = int(input())

    if op == 1:
        alimento = int(input('Alimentar todos com: '))
        for i in range(3):
            fazenda[i].alimentar(alimento)
    elif op == 2:
        brinquedo = int(input('Brincar todos com: '))
        for i in range(3):
            fazenda[i].brincar(brinquedo)
    elif op == 3:
        for i in range(3):
            print(fazenda[i].get_nome() + ': ' + str(fazenda[i].humor()))
    elif op == 4:
        break
