from abc import ABC, abstractmethod
#Criação dos da fábrica abstrata e dos produtos abstratos

class EventoPrincipal(ABC):
    @abstractmethod
    def print_evento_principal(self,name:str):
        pass
    @abstractmethod
    def registrar_participante_principal(self,participante:str):
        pass
class EventoComplementar(ABC):
    @abstractmethod
    def print_evento_complementar(self,name:str ):
        pass
    def registrar_participante_complementar(self,participante:str):
        pass

class EventAbstractFactory(ABC):
    @abstractmethod
    def create_evento_principal(self) -> EventoPrincipal:
        pass
    @abstractmethod
    def create_evento_complementar(self) -> EventoComplementar:
        pass



#Criação das fábricas concretas e dos produtos concretos

class EventoPresencialFactory(EventAbstractFactory):
    def create_evento_principal(self) -> EventoPrincipal:
        return EventoPresencialPrincipal()
    def create_evento_complementar(self) -> EventoComplementar:
        return EventoPresencialComplementar()

class EventoOnlineFactory(EventAbstractFactory):
    def create_evento_principal(self) -> EventoPrincipal:
        return EventoOnlinePrincipal()
    def create_evento_complementar(self) -> EventoComplementar:
        return EventoOnlineComplementar()


class EventoPresencialPrincipal(EventoPrincipal):
    def print_evento_principal(self,name:str):
        print("Evento presencial principal: "+name)
    def registrar_participante_principal(self, participante: str):
        print("Participante do evento presencial principal registrado com nome",participante)
class EventoPresencialComplementar(EventoComplementar):
    def print_evento_complementar(self,name:str):
        print("Evento presencial complementar: "+name)
    def registrar_participante_complementar(self, participante: str):
        print("Participante do evento presencial complementar registrado com nome",participante)

class EventoOnlinePrincipal(EventoPrincipal):
    def print_evento_principal(self,name:str):
        print("Evento online principal:"+name)
    def registrar_participante_principal(self, participante: str):
        print("Participante do evento online principal registrado com nome",participante)
class EventoOnlineComplementar(EventoComplementar):
    def print_evento_complementar(self,name:str):
        print("Evento online complementar: "+name)
    def registrar_participante_complementar(self, participante: str):
         print("Participante do evento online complementar registrado com nome",participante)


#Criação do objeto da fábrica concreta para egstão de eventos presenciais

gestaoEventoPresencial=EventoPresencialFactory()

#Vamos criar dois eventos principais, um complementar e um de networking

evento_principal_1=gestaoEventoPresencial.create_evento_principal()
evento_principal_2=gestaoEventoPresencial.create_evento_principal()
evento_complementar=gestaoEventoPresencial.create_evento_complementar()
#Mostrando os eventos presenciais

evento_principal_1.print_evento_principal("Conferência A")
evento_principal_1.registrar_participante_principal("André")
evento_principal_1.registrar_participante_principal("Almeida")
evento_principal_2.print_evento_principal("Conferência B")
evento_principal_2.registrar_participante_principal("Gustavo")
evento_complementar.print_evento_complementar("Workshop A")
evento_complementar.registrar_participante_complementar("Norberto")

gestaoEventoOnline=EventoOnlineFactory()

evento_principal_online_1=gestaoEventoOnline.create_evento_principal()
evento_complementar_online=gestaoEventoOnline.create_evento_complementar()
evento_principal_online_1.print_evento_principal("Conferência Online A")
evento_principal_online_1.registrar_participante_principal("Natália")
evento_principal_online_1.registrar_participante_principal("Gabriela")
evento_complementar_online.print_evento_complementar("Workshop Online A")
evento_complementar_online.registrar_participante_complementar("Suzana")

