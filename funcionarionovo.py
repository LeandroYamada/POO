class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def aumentar_salario(self, porcentagem_de_aumento=0):
        self.salario += self.salario * (porcentagem_de_aumento) / 100



func = Funcionario('Leandro', 5000)
print('Nome:', func.get_nome(), ', Salario', func.get_salario())
func.aumentar_salario(10)
print('Nome:', func.get_nome(), ', Salario', func.get_salario())
