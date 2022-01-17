class Tv:
    def __init__(self):
        self.canal = 0
        self.volume = 0

    def setcanal(self, canal):
        if (canal > 0) and (canal <= 100):
            self.canal = canal

    def aumentarvolume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuirvolume(self):
        if self.volume > 0:
            self.volume -= 1


tv = Tv()
print(vars(tv))
tv.setcanal(55)
print(vars(tv))
tv.aumentarvolume()
print(vars(tv))
tv.diminuirvolume()
print(vars(tv))
