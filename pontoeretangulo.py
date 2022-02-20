class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def valores_ponto(self):
        print(self.x, self.y)


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def centro(self):
        x_centro = (self.largura.x + self.altura.x) / 2.0
        y_centro = (self.largura.y + self.altura.y) / 2.0
        return ' X=' + str(x_centro) + ' Y=' + str(y_centro)


x1 = float(input('Entre com a coordenada x do canto inferior esquerdo: '))
y1 = float(input('Entre com a coordenada y do canto inferior esquerdo: '))
canto1 = Ponto(x1, y1)

x2 = float(input('Entre com a coordenada x do canto superior direito: '))
y2 = float(input('Entre com a coordenada y do canto superior direito: '))
canto2 = Ponto(x2, y2)

ret = Retangulo(canto1, canto2)
print('Ponto central é: %s' % ret.centro())
