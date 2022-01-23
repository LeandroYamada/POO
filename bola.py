class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        return self.cor


b = Bola("azul", 10, 'couro')
print(b.mostra_cor())
b.troca_cor('vermelha')
print(b.mostra_cor())
