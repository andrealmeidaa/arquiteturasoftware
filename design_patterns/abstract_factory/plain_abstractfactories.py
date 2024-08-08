from abc import ABC, abstractmethod
#Criação dos da fábrica abstrata e dos produtos abstratos

class EventoPrincipal(ABC):
    @abstractmethod
    def print_evento_principal(self,name:str):
        pass
class EventoComplementar(ABC):
    @abstractmethod
    def print_evento_complementar(self,name:str ):
        pass
class EventoNetworking(ABC):
    @abstractmethod
    def print_evento_networking(self,name:str):
        pass

class EventAbstractFactory(ABC):
    @abstractmethod
    def create_evento_principal(self) -> EventoPrincipal:
        pass

    @abstractmethod
    def create_evento_complementar(self) -> EventoComplementar:
        pass
    @abstractmethod
    def create_evento_networking(self) -> EventoNetworking:
        pass



#Criação das fábricas concretas e dos produtos concretos

class EventoPresencialFactory(EventAbstractFactory):
    def create_evento_principal(self) -> EventoPrincipal:
        return EventoPresencialPrincipal()
    def create_evento_complementar(self) -> EventoComplementar:
        return EventoPresencialComplementar()
    def create_evento_networking(self) -> EventoNetworking:
        return EventoPresencialNetworking()

class EventoOnlineFactory(EventAbstractFactory):
    def create_evento_principal(self) -> EventoPrincipal:
        return EventoOnlinePrincipal()
    def create_evento_complementar(self) -> EventoComplementar:
        return EventoOnlineComplementar()
    def create_evento_networking(self) -> EventoNetworking:
        return EventoOnlineNetworking()

class EventoPresencialPrincipal(EventoPrincipal):
    def print_evento_principal(self,name:str):
        print("Evento presencial principal: "+name)
class EventoPresencialComplementar(EventoComplementar):
    def print_evento_complementar(self,name:str):
        print("Evento presencial complementar: "+name)
class EventoPresencialNetworking(EventoNetworking):
    def print_evento_networking(self,name):
        print("Evento presencial networking: "+name)

class EventoOnlinePrincipal(EventoPrincipal):
    def print_evento_principal(self,name:str):
        print("Evento online principal:"+name)

class EventoOnlineComplementar(EventoComplementar):
    def print_evento_complementar(self,name:str):
        print("Evento online complementar: "+name)

class EventoOnlineNetworking(EventoNetworking):
    def print_evento_networking(self,name:str):
        print("Evento online networking: "+name)

#Criação do objeto da fábrica concreta para egstão de eventos presenciais

gestaoEventoPresencial=EventoPresencialFactory()

#Vamos criar dois eventos principais, um complementar e um de networking

evento_principal_1=gestaoEventoPresencial.create_evento_principal()
evento_principal_2=gestaoEventoPresencial.create_evento_principal()
evento_complementar=gestaoEventoPresencial.create_evento_complementar()
evento_networking=gestaoEventoPresencial.create_evento_networking()
#Mostrando os eventos presenciais

evento_principal_1.print_evento_principal("Conferência A")
evento_principal_2.print_evento_principal("Conferência B")
evento_complementar.print_evento_complementar("Workshop A")
evento_networking.print_evento_networking("Rodada de Negócios A")

gestaoEventoOnline=EventoOnlineFactory()

evento_principal_online_1=gestaoEventoOnline.create_evento_principal()
evento_networking_online=gestaoEventoOnline.create_evento_networking()
evento_complementar_online=gestaoEventoOnline.create_evento_complementar()
evento_principal_online_1.print_evento_principal("Conferência Online A")
evento_complementar_online.print_evento_complementar("Workshop Online A")
evento_networking_online.print_evento_networking("Rodada de Negócios Online A")