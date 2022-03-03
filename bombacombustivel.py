class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def alterar_valor(self, valor_litro):
        self.valor_litro = valor_litro

    def alterar_combustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel

    def alterar_qtd_combustivel(self, qtd_combustivel):
        self.quantidade_combustivel = qtd_combustivel

    def abastecer_por_valor(self, valor):
        temp2 = valor/self.valor_litro
        self.alterar_qtd_combustivel(self.quantidade_combustivel + temp2)
        return valor

    def abastecer_por_litro(self, qtd_litros):
        temp = qtd_litros * self.valor_litro
        self.alterar_qtd_combustivel(self.quantidade_combustivel + qtd_litros)
        return temp


b = BombaCombustivel('Gasolina', 7, 100)
print(b.alterar_valor(8))
print(b.valor_litro)
b.alterar_combustivel('etanol')
print(b.tipo_combustivel)

print(b.abastecer_por_litro(10))
print(b.abastecer_por_valor(80))
print(vars(b))
