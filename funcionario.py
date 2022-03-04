class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario


func = Funcionario('Leandro', 2000)
print('Nome:', func.get_nome(), ', Salario', func.get_salario())
