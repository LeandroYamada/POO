class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def ver_bucho(self):
        print(self.nome, ', Bucho: ', self.bucho)

    def digerir(self):
        if len(self.bucho) > 0:
            self.bucho.pop(0)


mac1 = Macaco('Macaco 1')
mac2 = Macaco('Macaco 2')

mac1.comer('Banana')
mac1.ver_bucho()

mac1.comer('Melancia')
mac1.ver_bucho()

mac1.comer('Uva')
mac1.ver_bucho()
mac1.digerir()
mac1.ver_bucho()

mac2.comer('Morango')
mac2.ver_bucho()

mac2.comer('Abacate')
mac2.ver_bucho()

mac2.comer('Kiwi')
mac2.ver_bucho()

mac2.comer(mac1)
mac2.ver_bucho()
