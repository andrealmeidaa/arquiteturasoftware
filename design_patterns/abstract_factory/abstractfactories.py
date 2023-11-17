from abc import ABC, abstractmethod
# Criaçao de classes abstratas em Python - https://docs.python.org/3/library/abc.html
# Interfaces da fabrica abstrata
class PaymentFactory(ABC):
    @abstractmethod
    def create_payment_processor(self):
        pass

    @abstractmethod
    def create_payment_serializer(self):
        pass

# Interface dos produtos abstratos
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, payment_data):
        pass

class PaymentSerializer(ABC):
    @abstractmethod
    def validate_payment(self, payment_data):
        pass
