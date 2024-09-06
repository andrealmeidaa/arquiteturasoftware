from abc import ABC

class Empregado(ABC):
    def __init__(self,nome:str):
        self.nome=nome
    def get_pagamento(self):
        raise NotImplementedError("Subclasses precisam implementar o método")

class EmpregadoFixo(Empregado):
    def __init__(self, nome:str, salario:float):
        super().__init__(nome=nome)
        self.salario = salario

    def get_pagamento(self):
        return self.salario

class Freelancer(Empregado):
    def __init__(self, nome:str, valor_hora:float, horas_trabalhadas:int):
        super().__init__(nome=nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas= horas_trabalhadas

    def get_pagamento(self):
        return self.valor_hora * self.horas_trabalhadas

class GestaoRH:
    def processar_pagamento(self,empregado:Empregado):
        print(f'Pagando {empregado.nome}: {empregado.get_pagamento()}')

if __name__=='__main__':
    joao=EmpregadoFixo(nome='João Maria',salario=1500)
    denise=Freelancer(nome='Denise Lima',valor_hora=34.56,horas_trabalhadas=80)
    gestorRH=GestaoRH()
    gestorRH.processar_pagamento(joao)
    gestorRH.processar_pagamento(denise)