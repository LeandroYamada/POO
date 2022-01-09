class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def setcomprimento(self, comprimento):
        self.comprimento = comprimento

    def setlargura(self, largura):
        self.largura = largura

    def getcomprimento(self):
        return self.comprimento

    def getlargura(self):
        return self.largura

    def area(self):
        return self.comprimento * self.largura

    def perimetro(self):
        return (2 * self.comprimento) + (2 * self.largura)


comp = float(input('Informe o valor de comprimento do retangulo: '))
larg = float(input('Informe o valor de largura do retangulo: '))

r = Retangulo(comp, larg)
print('A area do retangulo é: ', r.area())
print('o perimetro do retangulo é: ', r.perimetro())
