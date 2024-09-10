''''
Princípio da Segregação de Interfaces (ISP)

O Princípio da Segregação de Interfaces (ISP) é um dos cinco princípios SOLID. No ISP, 
a ideia é que uma classe não deve ser forçada a implementar métodos que não são utilizados. 
Em outras palavras, uma classe não deve ser forçada a implementar métodos que não 
são relevantes para ela.

O exemplo abaixo é uma versão aderente ao ISP quando comparado com o cenário colocado em vioa-isp.py.
A interface EmpregadoTI foi desmembrada em três interfaces distintas: Codificador, Designer e Testador.
Da mesma forma que agora temos três classes concretas: Desenvolvedor, UXDesigner e EngenheiroQA
que implementam apenas os métodos que são relevantes para elas.

'''

class Codificador:
    def programar(self):
        pass

class Designer:
    def design(self):
        pass

class Testador:
    def testar(self):
        pass

class Desenvolvedor(Codificador):
    def programar(self):
        print("Agora eu só programo")

class UXDesigner(Designer):
    def design(self):
        print("Designing da interface gráfica")

class EngenheiroQA(Testador):
    def testar(self):
        print("Testando a aplicação")

if __name__ == "__main__":
    desenvolvedor = Desenvolvedor()
    desenvolvedor.programar()

    designer = UXDesigner()
    designer.design()

    testador = EngenheiroQA()
    testador.testar()