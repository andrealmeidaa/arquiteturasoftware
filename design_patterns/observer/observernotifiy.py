from abc import ABC,abstractmethod

class EventObserver(ABC):
    @abstractmethod
    def update(self,msg:str):
        pass

class EventManager():
    def __init__(self) -> None:
        self.observers=[]
    def notify(self,msg:str)->None:
        for observer in self.observers:
            observer.update(msg)
    def registerObserver(self,observer:EventObserver):
        self.observers.append(observer)
        
class EmailNotifier(EventObserver):
    def update(self,msg: str):
        print(f'Notificação por e-mail:{msg}')
class PushNotifier(EventObserver):
    def update(self,msg: str):
        print(f'Notificação Push: {msg}')


manager=EventManager()
emailGoogle=EmailNotifier()
emailYahoo=EmailNotifier()
pushRSS=PushNotifier()
manager.registerObserver(emailGoogle)
manager.registerObserver(emailYahoo)
manager.registerObserver(pushRSS)

manager.notify('Mensagem importante!')
        