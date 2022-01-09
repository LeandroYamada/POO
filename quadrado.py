class Quadrado():
    def __init__(self, lado):
        self.setLado(lado)

    def setLado(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado

    def calcularArea(self, ):
        return self.lado * self.lado

q = Quadrado(5)
print(q.getLado())
q.setLado(10)
print(q.calcularArea())
