class Empregado:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_salario(self):
        return self.salario

class Freelancer(Empregado):
    def __init__(self, nome,valor_hora, horas_trabalhadas):
        super().__init__(nome, 0)  # Freelancers não têm salário fixo
        self.valor_hora = valor_hora
        self.horas_trabalhadas= horas_trabalhadas

    def get_salario(self):
        raise Exception("Freelancers não têm salário fixo")

