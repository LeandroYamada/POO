class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.nivel_combustivel = 0

    def andar(self, distancia):
        temp = distancia / self.consumo
        self.nivel_combustivel -= temp

    def obter_gasolina(self):
        return self.nivel_combustivel

    def adicionar_gasolina(self, qtd_gasolina):
        self.nivel_combustivel += qtd_gasolina


meu_fusca = Carro(25)
meu_fusca.adicionar_gasolina(55)
meu_fusca.andar(500)
print(vars(meu_fusca))
print(meu_fusca.obter_gasolina())