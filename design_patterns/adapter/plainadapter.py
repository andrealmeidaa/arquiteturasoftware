from abc import ABC, abstractmethod

class InterfaceAnimal(ABC):
    @abstractmethod
    def fazer_barulho(self):
        pass

class Cachorro(InterfaceAnimal):
    def fazer_barulho(self):
        return "Au au!"

class Gato():
    def miar(self):
        return "Miau!"

class AdaptadorDeAnimal(InterfaceAnimal,Gato):
    def __init__(self, gato):
        self.animal= gato

    def fazer_barulho(self):
        return self.animal.miar()

if __name__ == "__main__":
    cachorro = Cachorro()
    gato = Gato()
    print(cachorro.fazer_barulho())
    print(gato.miar())
    adaptador_de_gato = AdaptadorDeAnimal(gato)
    print(adaptador_de_gato.fazer_barulho())