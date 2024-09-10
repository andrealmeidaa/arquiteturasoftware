class EmpregadoTI:
    def programar(self):
        pass

    def design(self):
        pass

    def testar(self):
        pass
#Claramente não é um desenvolvedor fullstack
class Desenvolvedor(EmpregadoTI):
    def programar(self):
        print("Programando")

    def design(self):
        raise Exception("Desenvolvedores não fazem design!")
    #Perdoem a licença poética
    def testar(self):
        raise Exception("Desenvolvedores não fazem testes!")

if __name__ == "__main__":
    desenvolvedor = Desenvolvedor()
    desenvolvedor.programar()
    desenvolvedor.design()
    desenvolvedor.testar()