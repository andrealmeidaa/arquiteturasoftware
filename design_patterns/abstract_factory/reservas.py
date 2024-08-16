from abc import ABC,abstractmethod

class Quarto(ABC):
    @abstractmethod
    def descricao(self):
        pass

class ProcessoReserva(ABC):
    @abstractmethod
    def reservar(self):
        pass

class Pagamento(ABC):
    @abstractmethod
    def pagar(self):
        pass
class ReservaFactory(ABC):
    @abstractmethod
    def criarQuarto(self)->Quarto:
        pass
    @abstractmethod
    def processarReserva(self)->ProcessoReserva
        pass
    